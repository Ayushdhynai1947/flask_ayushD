
from flask import Blueprint
from flask_restful import Resource,Api
from flask import request

from app.utils.mysql.mysql_client import MySQLClient
from app.utils.config.config_client import ConfigClient





class MySQLResource(Resource):
    
    def get(self):
        config =ConfigClient(env='dev')
        mysql_uri = config.get_value("Database","uri")
        mysql_client=MySQLClient(mysql_uri)
        
        
        
        #updation neended
        # update_staus = mysql_client.update(table='product',column_values={'end_date':'31-Dec-24'},filter_condition=f"where oem = 'Zebra'")
        update =mysql_client.make_connection()
        # update =mysql_client.put()
        # update = mysql_client.update(table='produt',column_value={'end_date':'31-Dec-24'},filter_condition=f"where oem = 'Zebra'")
        
        # return {'all details are ':update}
        return {'all details are ':str(update)}
    
        
        #any operation can run 
        
    def post(self):
        return {'message':' Post request received '}




# from flask_restful import Resource, reqparse, abort, fields, marshal_with
# from app.models import USER




# resource_fields={
#     'emp_no':fields.Integer,
#     'product_name':fields.String,
#     'first_name':fields.String,
#     'last_name':fields.String,
    
# }



# class Todos(Resource):
#     @marshal_with(resource_fields)
#     def get(self):
#         tasks = USER.query.all()
#         return tasks, 200
    

