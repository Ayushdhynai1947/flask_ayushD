from flask_restful import Resource
from app.utils.mysql.mysql_client import MySQLClient
from app.utils.config.config_client import ConfigClient




class MySQLResource(Resource):
    
    def get(self):
        config =ConfigClient(env='dev')
        mysql_uri = config.get_value("Datbase","uri")
        mysql_client=MySQLClient(mysql_uri)
        
        #updation neend
        
        return {'message':" "}
        
        #any operation can run 
        
    # def post(self):
    #     return {'message':' '}




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
    

