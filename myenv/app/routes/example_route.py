from flask import Blueprint
# from flask_restful import Api
from app.resources.my_sqlresource import MySQLResource
from app.resources.csv_resource import CsvResouce


















#creating a blure print for route
example_route =Blueprint('example_route',__name__)













# Add  resource(s) to the blueprint
mysql_resourcse =MySQLResource()
mycsv_resourcse =CsvResouce()







#Define a route within the Bluepint
example_route.add_url_rule('/mysql', view_func=mysql_resourcse.as_view('mysql'))
example_route.add_url_rule('/mycsv', view_func=mycsv_resourcse.as_view('mycsv'))

