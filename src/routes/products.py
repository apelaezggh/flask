from math import prod
from flask import Blueprint, jsonify, request

from models.entities.product import Product
from models.products_model import ProductModel 

main = Blueprint('products_blueprint', __name__)

@main.route('/')
def get_products():
    try:
        products = ProductModel.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_product(id):
    try:
        product = ProductModel.get_product(id)
        if product != None:
            return jsonify(product)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/', methods=['POST'])
def add_product():
    try:
        id = request.json['id']
        name = request.json['name'] 
        unit_measure = request.json['unit_measure'] 

        product=Product(id, name, unit_measure)

        affected_row=ProductModel.add_product(product)

        if affected_row==1:
            return jsonify({'message': "Inserted product"}), 200
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>', methods=['DELETE'])
def delete_product(id):
    try:

        product=Product(id)

        affected_row=ProductModel.delete_product(product)

        if affected_row==1:
            return jsonify({'message': "Delete product"}), 200
        else:
            return jsonify({'message': "Error on delete"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>', methods=['PUT'])
def update_product(id):
    try:
        name = request.json['name'] 
        unit_measure = request.json['unit_measure'] 

        product=Product(id, name, unit_measure)

        affected_row=ProductModel.update_product(product)

        if affected_row==1:
            return jsonify({'message': "Updated product"}), 200
        else:
            return jsonify({'message': "Error on update"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500