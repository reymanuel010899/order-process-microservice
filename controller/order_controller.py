from model.order import Order
from services import OrderService
from fastapi.responses import JSONResponse


class OrderController:
    def __init__(self):
        self.order_service = OrderService()

    async def create_order(self, order_data: dict):
        try:
            new_order =  await self.order_service.create_order(order_data)
            if "error" in new_order:
                return JSONResponse(
                    content=new_order,
                    status_code=new_order.get("status_code", 500)
                )
            return new_order
        except ValueError as e:
            return JSONResponse(
                content={"error": str(e)},
                status_code=400
            )
        except Exception as e:
            return JSONResponse(
                content={"error": f"An unexpected error occurred. {str(e)}"},
                status_code=500
            )
    async def get_order(self, order_id: int):
        try:
            order = await self.order_service.get_order(order_id)
            if "error" in order:
                return JSONResponse(
                    content=order,
                    status_code=order.get("status_code", 500)
                )
            return order
        except ValueError as e:
            return JSONResponse(
                content={"error": str(e)},
                status_code=400
            )
        except Exception as e:
            return JSONResponse(
                content={"error": f"An unexpected error occurred. {str(e)}"},
                status_code=500
            )

    
    async def update_order(self, order_id, order_data: Order):
        try:
            order = await self.order_service.update_order(order_id, order_data)
            if "error" in order:
                return JSONResponse(
                    content=order,
                    status_code=order.get("status_code", 500)
                )
            return order
        except ValueError as e:
            return JSONResponse(
                content={"error": str(e)},
                status_code=400
            )
        except Exception as e:
            return JSONResponse(
                content={"error": f"An unexpected error occurred. {str(e)}"},
                status_code=500
            )
