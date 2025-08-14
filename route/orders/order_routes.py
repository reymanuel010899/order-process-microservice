from fastapi import APIRouter, HTTPException
from model.order import Order
from model.database import orders_collection
from typing import List

router = APIRouter()

# Crear un pedido
@router.post("/create", response_model=Order)
async def create_order(order: Order):
    existing_order = await orders_collection.find_one({"order_id": order.order_id})
    if existing_order:
        raise HTTPException(status_code=400, detail="Order ID already exists")
    
    order_dict = order.model_dump()
    await orders_collection.insert_one(order_dict)
    return order

# get all orders
@router.get("/get-all", response_model=List[Order])
async def get_orders():
    orders = []
    cursor = orders_collection.find()
    async for order in cursor:
        order["_id"] = str(order["_id"])
        orders.append(order)
    return orders

# get order by order_id
@router.get("/{order_id}", response_model=Order)
async def get_order(order_id: int):
    order = await orders_collection.find_one({"order_id": order_id})
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order["_id"] = str(order["_id"])
    return order

# update order
@router.put("/{order_id}", response_model=Order)
async def update_order(order_id: int, updated_order: Order):
    order_dict = updated_order.model_dump()
    result = await orders_collection.update_one(
        {"order_id": order_id},
        {"$set": order_dict, "$currentDate": {"updated_at": True}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order = await orders_collection.find_one({"order_id": order_id})
    order["_id"] = str(order["_id"])
    return order

# delete order
@router.delete("/{order_id}")
async def delete_order(order_id: int):
    result = await orders_collection.delete_one({"order_id": order_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": f"Order {order_id} deleted successfully"}
