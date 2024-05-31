# run.py
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

from app.resources import ProductList, ProductDetail
from app.auth import auth_bp
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)

api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<string:product_id>')
app.register_blueprint(auth_bp, url_prefix='/auth')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Product API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
