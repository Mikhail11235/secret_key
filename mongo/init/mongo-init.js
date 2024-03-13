db.getSiblingDB("admin").auth(
    process.env.MONGO_INITDB_ROOT_USERNAME,
    process.env.MONGO_INITDB_ROOT_PASSWORD
);
db = db.getSiblingDB("secret_key");
db.secret.insertOne({ "key": "initTestKey", "value": "initTestValue", "expired_at": ISODate() });
db.secret.createIndex({ "expired_at": 1 }, {expireAfterSeconds: 1 });