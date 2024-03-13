from fastapi import APIRouter, HTTPException, status, Depends
from schemas.secret import CreateSecret, ShowSecret, ShowKey
from pymongo.collection import Collection
from db import get_mongo_db


router = APIRouter()


@router.get("/secret/{secret_key}", response_model=ShowSecret)
def get_secret(secret_key, db: Collection = Depends(get_mongo_db)):
    collection = db.secret
    secret = collection.find_one({"key": secret_key})
    if secret:
        collection.delete_one({"key": secret_key})
        return {"secret": secret["value"]}
    else:
        raise HTTPException(
            detail=f"Secret with key {secret_key} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )


@router.post("/generate", response_model=ShowKey)
def create_secret(secret: CreateSecret, db: Collection = Depends(get_mongo_db)):
    collection = db.secret
    data = {"value": secret.secret, "expired_at": secret.expired_at, "key": secret.key}
    result = collection.insert_one(data)
    if not secret.key:
        secret.key = str(result.inserted_id)
        collection.update_one({'_id': result.inserted_id}, {"$set": {"key": str(result.inserted_id)}})
    return secret
