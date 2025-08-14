from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "order_service")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

# Collection for orders
orders_collection = db["orders"]