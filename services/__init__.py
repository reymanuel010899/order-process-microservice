import random
from model.database import orders_collection
from datetime import datetime

class OrderService:
    def __init__(self):
        self.order_collection = orders_collection

    async def create_order(self, order_data: dict):
        if  len(order_data.items) == 0:
             return {
                'error': 'items not found',
                'status_code': 404
            }

        order_dict = order_data.dict()
        order_dict["order_id"] = str(random.randint(1, 2**63 - 1))
        result = await self.order_collection.insert_one(order_dict)
        return await self.order_collection.find_one({"_id": result.inserted_id})

    async def get_order(self, order_id):
        order = await self.order_collection.find_one({"order_id": order_id})
        if not order:
            return {
                "error": "Order not found",
                "status_code":  404
            }
        
        order["_id"] = str(order["_id"])
        return order


    async def update_order(self, order_id, updated_data):
        order_dict = updated_data.dict()
        order_dict["updated_at"] = datetime.utcnow()

        result = await self.order_collection.update_one(
            {"order_id": order_id},
            {"$set": order_dict}
        )
        
        if result.matched_count == 0:
            return {
                "error": "Order not found",
                "status_code": 404
            }
        
        order = await orders_collection.find_one({"order_id": order_id})
        order["_id"] = str(order["_id"])
        return order

