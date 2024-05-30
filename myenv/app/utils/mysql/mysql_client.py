import mysql.connector
import json
from datetime import date

# from flask.views import MethodView







class MySQLClient():
    
    
    # def __init__(self,mysql_uri) -> None:
    #     self.mysql_uri =mysql_uri
    #     self.db  =self.make_connection()
    #     if self.db:
    #         self.cursor=self.db.cursor()
    #     else:
    #         self.cursor=None
    #     # self.db =db_conn if self.make_connection() else None
    #     # self.cursor =self.db.cursor()
    
    
    # def make_connection(self):
    #     db = None
    #     try :
    #        config = {
    #             'user': self.mysql_uri.split('://')[1].split(':')[0],
    #             'password': self.mysql_uri.split(':')[2].split('@')[0],
    #             'host': self.mysql_uri.split('@')[1].split('/')[0],
    #             'database': self.mysql_uri.split('/')[3]
    #         }
    #     #    print([config['host'],config['user'],config['password'],config['database']])
    #        db = mysql.connector.connect(**config)
    #        self.cursor = self.db.cursor(dictionary= True)
          
    #        print("connection succesfuly form")
    #     except Exception as e:
    #         error_message =f"Datbase connection fails{e}"
    #         print(error_message)
    #         raise ConnectionError(error_message)
    #     return db
   
   

    
    # def select(self,table_name,columns=None,filter_condition=None):
    #     # update_staus = mysql_client.select(table='product',column_values={'end_date':'31-Dec-24'},filter_condition=f"where first_name ='teddy')
    #     result =[]
    #     try:
    #         if self.db is not None:
    #             if columns is None:
    #                 query =f"SELECT * FROM {table_name}"
    #             else:
    #                 columns_c=','.join(columns)
    #                 query =f"SELECT {columns} FROM {table_name}"
    #                 if filter_condition:
    #                     query +=f"WHERE {filter_condition}"
    #                 self.cursor.execute(query)
    #                 result =self.cursor.fetchall()
    #                 return json.dumps(result)
    #         else:
    #             raise ConnectionError("Datatbase connection is not establish")
            
    #     except Exception as e:
    #         error_message = f"Failed to execute"
            
            
            
#########################################################################################################
    def __init__(self,mysql_uri) -> None:
        self.mysql_uri =mysql_uri
        try:
            # mysql_uri = "mysql://myuser:mypassword@localhost:3306/mydatabase"
            self.con=mysql.connector.connect(host="localhost",user="root",password="ayush",database="employees")
            self.cur= self.con.cursor(dictionary=True)
            print("Connection Scccesful")
        
        except:
            print("error genertaion")
            
            
    def get(self):
        self.cur.execute("SELECT * FROM  employees")
        result =self.cur.fetchall()
        # print(result)
        if len(result)>0:
            return json.dumps(result,default=self.json_serial)
        else:
            return "not data found"
    
    @staticmethod
    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, date):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")
        
        
    def post(self,data):
        self.cur.execute(f"SELECT  * FROM employees ")
    
    
    def put(self,data):
        self.cur.execute(f"INSERT INTO  employee(empno,birth_date,first_name,last_name,gender,hire_date) VALUES('{data['empno']}','{data['birth_date']}','{data['first_name']}','{data['last_name']}',{data['gender']},{data['hire_date']})")
        return "User Create Successful"
        
        
        
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
                    
                    
        
        
        
    
           
        #    if len(db)>0:
        #        return "Database connection created successfully!"
        #    else:
        #        error_mesaage =f"Database connection created suceesful"
        #        raise ConnectionError(error_mesaage)
        # except 
           
    
    
    
    
    
    
    
    