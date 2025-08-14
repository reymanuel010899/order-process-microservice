from datetime import datetime
from pydantic import BaseModel

class OrderCreateRequest(BaseModel):
    customer_name: str
    product_id: int
    quantity: int
    address: str

    class Config:
        schema_extra = {
            "example": {
                "customer_name": "John Doe",
                "product_id": 123,
                "quantity": 2,
                "address": "123 Main St, Springfield"
            }
        }