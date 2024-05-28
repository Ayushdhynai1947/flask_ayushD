from flask import Blueprint
from app.utils.mysql import MySQLClient

















#creating a blure print for route
example_route =Blueprint('example_route',__name__)












# Add  resource(s) to the blueprint
mysql_resourcse =MySQLClient()




#Define a route within the Bluepint
example_route.add_url_rule('/mysql',view_func=mysql_resourcse.as_view('mysql'))

