# app/models.py
from flask import current_app
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDB:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client.get_default_database()

    def get_collection(self, name):
        return self.db[name]

db = MongoDB(current_app.config['MONGO_URI'])

class Product:
    collection = db.get_collection('products')

    @staticmethod
    def get_all():
        return list(Product.collection.find())

    @staticmethod
    def get_by_id(product_id):
        return Product.collection.find_one({"_id": ObjectId(product_id)})

    @staticmethod
    def create(data):
        return Product.collection.insert_one(data)

    @staticmethod
    def update(product_id, data):
        return Product.collection.update_one({"_id": ObjectId(product_id)}, {"$set": data})

    @staticmethod
    def delete(product_id):
        return Product.collection.delete_one({"_id": ObjectId(product_id)})
