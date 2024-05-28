import mysql.connector
from flask.views import MethodView







class MySQLClient9(MethodView):
    
    def __init__(self) -> None:
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="ayush",database="employee")
        except:
            print("error genertaion")
        
        
        
    def user_getall_model(self):
        mysql.connector