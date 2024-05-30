from flask import Blueprint
# from flask_restful import Api
from app.resources.my_sqlresource import MySQLResource


















#creating a blure print for route
example_route =Blueprint('example_route',__name__)













# Add  resource(s) to the blueprint
mysql_resourcse =MySQLResource()







#Define a route within the Bluepint
example_route.add_url_rule('/mysql', view_func=mysql_resourcse.as_view('mysql'))

