import os
from dotenv import load_dotenv
load_dotenv()


class Settings(object):
    PROJECT_NAME = "Secret-Key"
    PROJECT_VERSION = "1.0.0"
    MONGO_DATABASE = os.environ.get("MONGO_INITDB_DATABASE")
    MONGO_USERNAME = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
    MONGO_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
    MONGO_SERVER = "mongodb" if os.environ.get("NOT_LOCAL") == "1" else "localhost"
    MONGO_PORT = os.environ.get("MONGO_PORT")
    MONGO_DB_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_SERVER}:{MONGO_PORT}" \
        "/admin?authSource=admin&authMechanism=SCRAM-SHA-1"


settings = Settings()
