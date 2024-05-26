from flask import Flask
from app.routes.example_route import example_route
from flask_cors import CORS

# Create an instance  of the 
import mysql.connector




def create_app():
    app= Flask(__name__)
    CORS(app)
    
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