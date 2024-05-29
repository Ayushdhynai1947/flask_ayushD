# from flask import Flask
# from flask_restful import Api
# from app.routes.example_route import example_route
# # from app.utils.config import config_client
# import mysql.connector
# # import os
# from flask_cors import CORS
# # from app.utils.config import DevelopmentConfig   # Adjust the import path as needed

# # from app.utils.mysql import MySQLClient
# # Create an instance  of the 





# def create_app():
#     app= Flask(__name__)
#     api =Api(app)
#     CORS(app)
    
    
    
#     # env = 'prod'
#     # app.config =config_client(env)
    
    
    
    
#     #set up data base URI
#     # app.config[SQLALCHEMY_DATABASE_URI] =app.config.get('SQLALCHEMY_DATABASE_URI')
    
    
    
#     # app.config.from_object(config_client('dev'))
#     # data_uri =app.config.get('SQLALCHEMY_DATABASE_URI')
#     # app.config['SQLALCHEMY_DATABASE_URI'] = data_uri
#     # CORS(app)
    
    
#     app.config['MYSQL_HOST']= 'localhost'
#     app.config['MYSQL_USER'] ='root'
#     app.config['MYSQL_PASSWORD'] = 'ayush'
#     app.config['MYSQL_DB'] = 'employee'
    
    
#     # # Create a MySQL connection
#     db = mysql.connector.connect(
#       host=app.config['MYSQL_HOST'],
#       user=app.config['MYSQL_USER'],
#       password=app.config['MYSQL_PASSWORD'],
#       database=app.config['MYSQL_DB']  )
    
    
#     # Register blueprints
#     app.register_blueprint(example_route,url_prefix='/api')
    
#     return app