from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config
from model.database import db
from route.orders.order_routes import router as order_router
app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=config.origins,  # Dominios permitidos
#     allow_credentials=True,
#     allow_methods=["*"],  # Métodos permitidos
#     allow_headers=["*"],  # Encabezados permitidos
# )

app = FastAPI(
    title="Order Process API",
    description="Microservice to process orders efficiently",
    version="1.0.0",
    contact={
        "name": "Rey Manuel",
        "email": "rey@example.com",
    }
)

app.include_router(
    order_router,
    prefix="/orders",
    tags=["orders"]
)
@app.get("/")
def read_root():
    return {"message": "successful health check-up 🚀"}


@app.on_event("startup")
async def startup_db_client():
    print("********")
    coleccion = db["mi_coleccion"]
   

    print("📦 Conexión a MongoDB iniciada.", coleccion )
