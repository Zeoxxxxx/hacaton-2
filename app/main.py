from fastapi import FastAPI
from app.routes import api_entpoint

app = FastAPI() # объявили наше приложение

app.include_router(api_entpoint.router, prefix="/auth") # тут установии роутеры
