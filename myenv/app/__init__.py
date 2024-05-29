from flask import Flask
from app.routes.example_route import example_route
from flask_cors import CORS
from app.utils.config import DevelopmentConfig  # Adjust the import path as needed
import os
from app.utils.mysql import MySQLClient
# Create an instance  of the 
import mysql.connector




def create_app():
    app= Flask(__name__)
    
    
    # env =os.getenv('FLASK_ENV','deelopment')
    # app.config.from_object('DevelopmentConfig')
    # data_uri =app.config.get('SQLALCHEMY_DATABASE_URI')
    # app.config['SQLALCHEMY_DATABASE_URI'] = data_uri
    # CORS(app)
    
    
    # app.config['MYSQL_HOST']= 'localhost'
    #app.config['MYSQL_USER'] ='root'
    # app.config['MYSQL_PASSWORD'] = 'root'
    # app.config['MYSQL_DB'] = 'srctrac'
    
    
    # # Create a MySQL connection
      # db = mysql.connector.connect(
      # host=app.config['MYSQL_HOST'],
      # user=app.config['MYSQL_USER'],
      # password=app.config['MYSQL_PASSWORD'],
      # database=app.config['MYSQL_DB'] # )
    
    
    # Register blueprints
    app.register_blueprint(example_route,url_prefix='/api')
    
    return app