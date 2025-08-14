from services.order_service import OrderService
from fastapi import JsonResponse

# order_services = OrderService()

# controller/order_controller.py
class OrderController:
    def __init__(self):
        self.order_service = OrderService()

    def create_order(self, order_data: dict):
        try:
            return self.order_service.create_order(order_data)
        except ValueError as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {"error": f"An unexpected error occurred. {str(e)}"},
                status=500
            )

    def get_order(self, order_id):
        return self.order_service.get_order(order_id)

    def update_order(self, order_id, order_data):
        return self.order_service.update_order(order_id, order_data)

    def delete_order(self, order_id):
        return self.order_service.delete_order(order_id)