import mysql.connector
import json
from flask.views import MethodView







class MySQLClient():
    
    # def __init__(self) -> None:
    #     try:
    #         # mysql_uri = "mysql://myuser:mypassword@localhost:3306/mydatabase"
    #         self.con=mysql.connector.connect(host="localhost",user="root",password="ayush",database="employee")
    #         self.cur= self.con.cursor(dictionary=True)
    #         print("Connection Scccesful")
        
    #     except:
    #         print("error genertaion")
            
            
    # def get(self):
    #     self.cur.execute("SELECT * FROM  employee")
    #     result =self.cur.fetchall()
    #     print(result)
    #     if len(result)>0:
    #         return  json.dump(result)
    #     else:
    #         return "not data found"
        
        
    
    # def put(self,data):
    #     self.cur.execute(f"INSERT INTO  employee(empno,birth_date,first_name,last_name,gender,hire_date) VALUES('{data['empno']}','{data['birth_date']}','{data['first_name']}','{data['last_name']}',{data['gender']},{data['hire_date']})")
    #     return "User Create Successful"
        
        
        
    # def update(self,data):
    #     self.cur.execute(f'UPDATE user SET empno ='{data['empno']}', birth_date='{data['birth_date']}',first_name='{data['first_name']}',last_name='{data['last_name']}',gender='{data['first_name']}',hire_date='{data['first_name']} 'WHERE  id ={data['id']}')
    #     if self.cur.rowcount>0:
    #         return "user update suceesfully"
    #     else:
    #         return "Nothing to update"
        
        
        
        
        
        
        
        
        
        
    # def user_getall_model(self):
    #     #qurey execution code
    #     self.cur.execute("SELECT * FROM users")
    #     result=self.cur.fetchall()
    #     if len(result)>0:
    #         return json.dumps(result)
    #     else:
    #         return "No data found"
        
    
    # def user_addOne_model(self)
    
    def __init__(self,mysql_uri) -> None:
        self.mysql_uri =mysql_uri
        db_conn =self.make_connection()
        self.db = db_conn if self.make_connection else None
        self.cursor =self.db.coursor()
    
    
    def make_connection(self):
        db = None
        try :
        #    config = {
        #         'user': self.mysql_uri.split('://')[1].split(':')[0],
        #         'password': self.mysql_uri.split(':')[2].split('@')[0],
        #         'host': self.mysql_uri.split('@')[1].split('/')[0],
        #         'database': self.mysql_uri.split('/')[3]
        #     }
           db = mysql.connector.connect(host="localhost",user="root",password="ayush",database="employee")
           
           if len(db)>0:
               return "Database connection created successfully!"
           else:
               error_mesaage =f"Database connection created suceesful"
               raise ConnectionError(error_mesaage)
        except 
           
    
    
    
    
    
    
    
    