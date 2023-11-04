from functools import wraps

# from flask import request, make_response, jsonify
#
# from model import user
# import datetime
# from api.ini_api import IAPI
#
# def authenticate(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if not("HTTP_AUTHORIZATION" in request.headers.environ):
#             return make_response(jsonify(message='No authorization'), 401)
#
#         re = request.headers.environ['HTTP_AUTHORIZATION']
#         rw = re.split(' ')
#         if rw[0] != 'Bearer':
#             return make_response(jsonify(message='No authorization'), 401)
#
#         us = user.user.checkSession(rw[1])
#         if us == None :
#             return make_response(jsonify(message='No session'), 401)
#         IAPI.US = us
#         fun = func(*args, **kwargs)
#         return fun
#
#     return wrapper


