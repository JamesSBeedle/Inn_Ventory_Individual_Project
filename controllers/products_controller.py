from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", inventory = products)

@products_blueprint.route("/products/<id>", methods=["GET"])
def show_product(id):
    product = product_repository.select(id)
    return render_template("/products/show.html", product = product)