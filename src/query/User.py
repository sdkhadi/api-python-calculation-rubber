import pymysql
from app import app
from helper.config import mysql
from flask import request,jsonify
import json

def queryCreateUser():
        try:        
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
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()
    
def queryGetUsers(query,params):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query,params)
            usersRows = cursor.fetchall()
            return usersRows
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()   

def queryGetUser(users_id):  
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, name, email, phone, address FROM users WHERE id =%s",users_id)
            usersRow = cursor.fetchone()
            respone = jsonify(usersRow)
            respone.status_code = 200
            return respone
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()  

def queryUpdateUsers():
        try:
            _json = request.json
            _id = _json['id']
            _name = _json['name']
            _email = _json['email']
            _phone = _json['phone']
            _address = _json['address']
            if _name and _email and _phone and _address and _id and request.method == 'PUT':			
                sqlQuery = "UPDATE users SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
                bindData = (_name, _email, _phone, _address, _id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sqlQuery, bindData)
                conn.commit()
                respone = jsonify('usersloyee updated successfully!')
                respone.status_code = 200
                return respone
            else:
                return showMessage()
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()

def queryDeleteUser(id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE FROM users WHERE id ="+id,None)
            conn.commit()
            respone = jsonify('usersloyee deleted successfully!')
            print(respone)

            respone.status_code = 200
            return respone
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()    

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
