from fastapi import FastAPI
from config import settings
from apis.base import api_router


def start_application():
    print(f"Mongodb uri: {settings.MONGO_DB_URI}")
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(api_router)
    return app


app = start_application()
