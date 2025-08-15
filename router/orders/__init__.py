
from fastapi.responses import JSONResponse
from controller import order_controller
from fastapi import APIRouter
from model.order import Order
from type_model.response import OrderRequest
from controller.order_controller import OrderController
order_controller = OrderController()
router = APIRouter()


@router.post(
    "/create",
    response_model=Order,
    summary="Create a new order",
    description=(
        "This endpoint allows you to **create a new order**. "
        "It receives the order details and returns the created order with its assigned ID."
    ),
    response_description="The newly created order with its details and assigned ID."
)
async def create_order(order_data: OrderRequest):
    try:
        return await order_controller.create_order(order_data)
    except ValueError as e:
        return JSONResponse(
                content={"error": str(e)},
                status_code=500
            )

@router.get(
    "/{order_id}",
    response_model=Order,
    summary="Get an order by its ID",
    description=(
        "This endpoint retrieves an order using its unique **order_id**. "
        "If the order does not exist, an error will be returned."
    ),
    response_description="The order details corresponding to the provided ID."
)
async def get_order(order_id: str):
    try:
        return await order_controller.get_order(order_id)
    except ValueError as e:
        return JSONResponse(
                content={"error": str(e)},
                status_code=400
            )
    

@router.patch(
    "/{order_id}",
    response_model=Order,
    summary="Update an existing order",
    description=(
        "This endpoint allows you to **partially update** an existing order by its ID. "
        "You can update one or more fields of the order."
    ),
    response_description="The updated order with the applied changes."
)
@router.patch("/{order_id}", response_model=Order)
async def update_order(order_id: str, updated_order: OrderRequest):
    try:
        return await order_controller.update_order(order_id, updated_order)
    except ValueError as e:
        return JSONResponse(
                content={"error": str(e)},
                status_code=400
            )