from flask import Blueprint, request
from app.models.product import Product
from util.response_codes import ResponseBuilder
from app import db

# 创建蓝图
products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/list", methods=["GET"])
def list_products():
    """
    获取所有产品列表的接口

    Returns:
        JSON: 包含产品列表的JSON响应
    """
    try:
        products = Product.query.all()
        return ResponseBuilder.build_success_response(data=products)
    except Exception as e:
        return ResponseBuilder.build_error_response(message=str(e))


@products_blueprint.route("/create", methods=["POST"])
def create_product():
    """
    创建新产品的接口

    Returns:
        JSON: 表示操作成功的JSON响应
    """
    try:
        if request.method == "POST":
            name = request.form["name"]
            price = float(request.form["price"])
            description = request.form["description"]

            new_product = Product(name=name, price=price, description=description)
            db.session.add(new_product)
            db.session.commit()

        return ResponseBuilder.build_success_response()
    except Exception as e:
        return ResponseBuilder.build_error_response(message=str(e))


@products_blueprint.route("/update/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """
    更新产品信息的接口

    Args:
        product_id (int): 产品ID

    Returns:
        JSON: 表示操作成功的JSON响应
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            return ResponseBuilder.build_error_response(message="Product not found")

        if request.method == "PUT":
            name = request.form["name"]
            price = float(request.form["price"])
            description = request.form["description"]

            product.name = name
            product.price = price
            product.description = description
            db.session.commit()

        return ResponseBuilder.build_success_response()
    except Exception as e:
        return ResponseBuilder.build_error_response(message=str(e))


@products_blueprint.route("/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """
    删除产品的接口

    Args:
        product_id (int): 产品ID

    Returns:
        JSON: 表示操作成功的JSON响应
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            return ResponseBuilder.build_error_response(message="Product not found")

        db.session.delete(product)
        db.session.commit()

        return ResponseBuilder.build_success_response()
    except Exception as e:
        return ResponseBuilder.build_error_response(message=str(e))
