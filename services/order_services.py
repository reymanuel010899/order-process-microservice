from model import order


class OrderServices:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def create_order(self, order_data: dict):
        # Validate and process order data

        if order_data.get('order_id') is None:
            raise ValueError("Order ID is required.")
        
        
        if not order_data.get('items'):
            raise ValueError("Order must contain at least one item.")
        
        # Create the order using the repository
        return self.order_repository.create(order_data)

    def get_order(self, order_id):
        # Retrieve an order by ID
        return self.order_repository.get(order_id)

    def update_order(self, order_id, updated_data):
        # Update an existing order
        return self.order_repository.update(order_id, updated_data)

    def delete_order(self, order_id):
        # Delete an order by ID
        return self.order_repository.delete(order_id)
    

