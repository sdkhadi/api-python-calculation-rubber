import pymysql
from config import mysql
from flask import request,jsonify
import json
def queryGetAll(query,params):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query,params)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()
def queryPostData(query,bindData):
    try:
        conn =mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query,bindData)
        conn.commit()
        result = '{"status code": 200, "success":true,"message":"Success Post Data"}'
        respone = json.loads(result)
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

def queryGetOneData(query,params):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, params)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

def queryDeleteData(query,bindData):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, bindData)
        conn.commit()
        result = '{"status code": 200, "success":true,"message":"Success Delete Data"}'
        respone = json.loads(result)
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
def queryUpdateData(query,bindData):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, bindData)
        conn.commit()
        result = '{"status code": 200, "success":true,"message":"Success Updated Data"}'
        response = json.loads(result)
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()