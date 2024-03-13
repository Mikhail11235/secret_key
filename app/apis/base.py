from fastapi import APIRouter
from apis import route_secret


api_router = APIRouter()
api_router.include_router(route_secret.router, prefix="", tags=["secret"])
