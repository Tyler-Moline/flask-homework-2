from flask import request, Response, Blueprint

import controllers

products = Blueprint('products', __name__)


@products.route("/category", methods=["GET"])
def product_get_all() -> Response:
    return controllers.wish_list_get_all(request)

@products.route("/categories", methods=["POST"])
def product_add() -> Response:
    return controllers.wish_list_add(request)

@products.route("/category/<category_id>", methods=["GET"])
def product_get_by_id(category_id) -> Response:
    return controllers.wish_list_update(request, category_id)

@products.route("/category/<category_id>", methods=["PUT"])
def product_update_by_id(category_id) -> Response:
    return controllers.wish_list_update(request, category_id)

@products.route("/category/delete/<category_id>", methods=["DELETE"])
def product_delete(category_id) -> Response:
    return controllers.wish_list_delete(request, category_id)