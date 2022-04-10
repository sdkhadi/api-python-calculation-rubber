from app import app
from flask import request,jsonify

@app.errorhandler(404)
def showMessage(errorMessage,statusCode):
    message = {
        'status': statusCode,
        'message': errorMessage,
    }
    respone = jsonify(message)
    respone.status_code = statusCode
    return respone