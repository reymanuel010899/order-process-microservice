from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: int
    customer_name: str
    customer_email: str
    customer_address: str
    items: List[OrderItem]
    total_price: float
    status: str = "pending"  # pending, shipped, delivered, cancelled
    payment_method: str  # e.g., "credit_card", "paypal"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
