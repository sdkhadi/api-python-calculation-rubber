from tkinter.messagebox import NO

from pymysql import NULL
from app import app
from flask import jsonify
import json
from helper.dbHelper import *
from helper.errors import *

@app.route('/create', methods=['POST'])
def create_users():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _phone = _json['phone']
    _address = _json['address']	
    if _name and _email and _phone and _address and request.method == 'POST':
        checkEmail = queryGetOneData("SELECT email FROM users WHERE email =%s", _email)
        print(checkEmail)
        if checkEmail is None:
            result = queryPostData("INSERT INTO users(name, email, phone, address) VALUES(%s, %s, %s, %s)",(_name, _email, _phone, _address))
            return result
        else:
            return showMessage("User Already Exist",404)
              
@app.route('/users')
def users():
    result = queryGetAll("SELECT id, name, email, phone, address FROM users",None)
    response = jsonify(result)
    response.status_code = 200
    return response

@app.route('/users/<users_id>', methods=['GET'])
def users_details(users_id):
    result = queryGetOneData("SELECT id, name, email, phone, address FROM users WHERE id =%s", users_id)
    return result

@app.route('/update', methods=['PUT'])
def update_users():
    _json = request.json
    _id = _json['id']
    _name = _json['name']
    _email = _json['email']
    _phone = _json['phone']
    _address = _json['address']
    if _name and _email and _phone and _address and _id and request.method == 'PUT':
        result = queryUpdateData("UPDATE users SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s",(_name, _email, _phone, _address, _id,))
        return result
    else:
        return showMessage()

@app.route('/delete/<id>', methods=['DELETE'])
def delete_users(id):
    result = queryDeleteData("DELETE FROM users WHERE id =%s", (id,))
    if result:
        return result
        
if __name__ == "__main__":
    app.run(debug=True)