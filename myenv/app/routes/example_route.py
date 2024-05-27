from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

















#creating a blure print for route
example_route =Blueprint('example_route',__name__)





#Define a route within the Bluepint
@example_route.route('/hello',methods=['Get'])
def heelo():
    return "heelo world"

