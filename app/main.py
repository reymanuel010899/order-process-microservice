from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config
from model.database import db
from route.orders import router as order_router

app = FastAPI(
    title="Order Process API",
    description="Microservice to process orders efficiently",
    version="1.0.0",
    contact={
        "name": "Rey Manuel",
        "email": "reymanuelferrera78@gmail.com",
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(
    order_router,
    prefix="/orders",
    tags=["Orders Management"]
)

@app.get("/", tags=["Health Check"])
def read_root():
    return {"message": "successful health check-up 🚀", "status": "running"}

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "healthy", "service": "order-process-microservice"}

@app.on_event("startup")
async def startup_db_client():
    coleccion = db["orders"]
    print("📦 Connection to MongoDB initiated.", coleccion)
