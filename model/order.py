from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import uuid

class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: int = Field(default_factory=lambda: uuid.uuid4().int >> 64, read_only=True)
    customer_name: str
    customer_email: str
    customer_address: str
    items: List[OrderItem]
    total_price: float
    status: str = "create" 
    payment_method: str  
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    uuid: str = Field(default_factory=lambda: str(uuid.uuid4()))
