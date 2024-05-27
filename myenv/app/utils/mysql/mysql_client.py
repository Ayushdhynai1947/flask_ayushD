import mysql.connector







class MySQLClient:
    
    def __init__(self) -> None:
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="ayush",database="employee")
        except:
            print("error genertaion")
        
        
        
    def user_getall_model(self):
        mysql.connector