from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class OrderRequest(BaseModel):
    customer_name: str
    customer_email: str
    customer_address: str
    items: List[OrderItem]  
    total_price: float
    status: str = "pending" 
    payment_method: str

    class Config:
        schema_extra = {
            "example": {
                "customer_name": "John Doe",
                "customer_email": "john.doe@example.com",
                "customer_address": "123 Main St, Springfield",
                "items": [
                    {
                        "product_id": "123",
                        "name": "Product Name",
                        "quantity": 2,
                        "price": 50.0
                    }
                ],
                "total_price": 100.0,
                "status": "pending",
                "payment_method": "credit_card"
            }
        }