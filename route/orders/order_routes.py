from fastapi import APIRouter, HTTPException
# from .model.order import Order
from database import orders_collection

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

# # Crear un pedido
# @router.post("/create", response_model=Order)
# def create_order(order: Order):
#     if orders_collection.find_one({"order_id": order.order_id}):
#         raise HTTPException(status_code=400, detail="Order ID already exists")
    
#     orders_collection.insert_one(order.dict())
#     return order

# # get all orders
# @router.get("/get-all", response_model=list[Order])
# def get_orders():
#     orders = list(orders_collection.find())
#     for o in orders:
#         o["_id"] = str(o["_id"])
#     return orders

# # get order by order_id
# @router.get("/{order_id}", response_model=Order)
# def get_order(order_id: int):
#     order = orders_collection.find_one({"order_id": order_id})
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     order["_id"] = str(order["_id"])
#     return order

# # update order
# @router.put("/{order_id}", response_model=Order)
# def update_order(order_id: int, updated_order: Order):
#     result = orders_collection.update_one(
#         {"order_id": order_id},
#         {"$set": updated_order.dict(), "$currentDate": {"updated_at": True}}
#     )
#     if result.matched_count == 0:
#         raise HTTPException(status_code=404, detail="Order not found")
    
#     order = orders_collection.find_one({"order_id": order_id})
#     order["_id"] = str(order["_id"])
#     return order

# # delete order
# @router.delete("/{order_id}")
# def delete_order(order_id: int):
#     result = orders_collection.delete_one({"order_id": order_id})
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return {"message": f"Order {order_id} deleted successfully"}
