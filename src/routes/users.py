from crypt import methods
from flask import Blueprint, jsonify, request

from models.entities.users import User
from models.users_model import UserModel 

main = Blueprint('users_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({'message': 'User not finded'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/', methods=['POST'])
def add_user():
    try:
        id = request.json['id']
        name = request.json['name'] 
        password = request.json['password'] 
        cell = request.json['cell'] 

        user=User(id, name, password, cell)

        affected_row=UserModel.add_user(user)

        if affected_row==1:
            return jsonify({'message': "Inserted user"}), 200
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>', methods=['DELETE'])
def delete_user(id):
    try:

        user=User(id)

        affected_row=UserModel.delete_user(user)

        if affected_row==1:
            return jsonify({'message': "Delete user"}), 200
        else:
            return jsonify({'message': "Error on delete"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>', methods=['PUT'])
def update_user(id):
    try:
        name = request.json['name'] 
        password = request.json['password'] 
        cell = request.json['cell'] 

        user=User(id, name, password, cell)

        affected_row=UserModel.update_user(user)

        if affected_row==1:
            return jsonify({'message': "Updated user"}), 200
        else:
            return jsonify({'message': "Error on update"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500