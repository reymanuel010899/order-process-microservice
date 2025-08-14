# from http.client import HTTPException
# from model import order
# from model.database import orders_collection

# class OrderServices:
#     def __init__(self, order_repository):
#         self.order_repository = order_repository
#         self.order_collection = orders_collection

#     def create_order(self, order_data: dict):
#         # Validate and process order data
#         print("Creating order with data:", order_data)
#         existing_order =  self.order_collection.find_one({"order_id": order_data.order_id})
#         if existing_order:
#             raise HTTPException(status_code=400, detail="Order ID already exists")
    
#         order_dict = order.model_dump()
#         return self.order_collection.insert_one(order_dict)

#     def get_order(self, order_id):
#         # Retrieve an order by ID
#         return self.order_repository.get(order_id)

#     def update_order(self, order_id, updated_data):
#         # Update an existing order
#         return self.order_repository.update(order_id, updated_data)

#     def delete_order(self, order_id):
#         # Delete an order by ID
#         return self.order_repository.delete(order_id)
    

