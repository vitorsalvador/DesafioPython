# app/schemas.py
from marshmallow import Schema, fields, validate

class ProductSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))
    description = fields.Str()
    stock = fields.Int(validate=validate.Range(min=0))
    

