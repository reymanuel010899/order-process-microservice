class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

    origins = [
        "http://localhost:3000"
        "http://127.0.0.1:5500",  
        "https://midominio.com",
    ]


config = Config()