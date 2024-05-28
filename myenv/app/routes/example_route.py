from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

















#creating a blure print for route
example_route =Blueprint('example_route',__name__)





#Define a route within the Bluepint
example_route.add_url_rule('/mysql',view_func=mysql_resource)

