# app/resources.py
from flask import request, jsonify
from flask_restful import Resource
from bson.json_util import dumps
from app.models import Product
from app.schemas import ProductSchema
from flask_jwt_extended import jwt_required

class ProductList(Resource):
    def get(self):
        products = Product.get_all()
        return jsonify(dumps(products))

    @jwt_required()
    def post(self):
        data = request.get_json()
        errors = ProductSchema().validate(data)
        if errors:
            return jsonify(errors), 400
        Product.create(data)
        return jsonify({"message": "Product created successfully"}), 201

class ProductDetail(Resource):
    def get(self, product_id):
        product = Product.get_by_id(product_id)
        if not product:
            return jsonify({"message": "Product not found"}), 404
        return jsonify(dumps(product))

    @jwt_required()
    def put(self, product_id):
        data = request.get_json()
        errors = ProductSchema().validate(data)
        if errors:
            return jsonify(errors), 400
        Product.update(product_id, data)
        return jsonify({"message": "Product updated successfully"})

    @jwt_required()
    def delete(self, product_id):
        Product.delete(product_id)
        return jsonify({"message": "Product deleted successfully"})
