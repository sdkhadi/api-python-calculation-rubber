import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import json

def queryCreateUser():
     _json = request.json
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']	
        if _name and _email and _phone and _address and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO users(name, email, phone, address) VALUES(%s, %s, %s, %s)"
            bindData = (_name, _email, _phone, _address)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            data_from_api = '{"status code": 200, "success":true,"message":"Success Create User"}'
            respone = json.loads(data_from_api)
            return respone
        else:
            return showMessage()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
