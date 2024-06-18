import mysql.connector
import json
from datetime import date

# from flask.views import MethodView







class MySQLClient():
    
    def __init__(self,mysql_uri) -> None:
        self.mysql_uri = mysql_uri
        db_conn = self.make_connection()
        self.db = db_conn
        if self.db:
            self.cursor=self.db.cursor(dictionary = True)
        else:
            self.cursor=None
        # self.db =db_conn if self.make_connection() else None
        # self.cursor =self.db.cursor()
    
    
    def make_connection(self):
        db = None
        try :
        #    config = {
        #         'user': self.mysql_uri.split('://')[1].split(':')[0],
        #         'password': self.mysql_uri.split(':')[2].split('@')[0],
        #         'host': self.mysql_uri.split('@')[1].split('/')[0],
        #         'database': self.mysql_uri.split('/')[3]
        #     }
        #    print([config['host'],config['user'],config['password'],config['database']])
        #    db = mysql.connector.connect(**config)
           db = mysql.connector.connect(host="localhost",user="root",password="ayush",database="employees")
          
           print("connection succesfuly form")
        except Exception as e:
            error_message =f"Datbase connection fails{e}"
            print(error_message)
            raise ConnectionError(error_message)
        return db
    
    
    
    
    def select(self, table_name, columns=None, filter_condition=None):
        results = []
        select_status = None
        try:
            if self.db is not None:
                if columns is None:
                    query = f"SELECT * FROM {table_name}"
                else:
                    columns_str = ','.join(columns)
                    query = f"SELECT {columns_str} FROM {table_name}"
                if filter_condition:
                    query += f" WHERE {filter_condition}"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                results = [dict(row) for row in rows]
                select_status = dict(status="success", results=results)
            else:
                error_message = "Please make the connection first"
                raise ConnectionError(error_message)
        except Exception as e:
            error_message = f"Failed to execute select: {e}"
            print(error_message)
            raise ConnectionError(error_message)
        return select_status
    
    
    def update (self, table, column_values,filter_condition =None):
        update_status = None
        try:
            set_clause = ",".join({f"{column}= %s" for column in column_values.key()})
            values  = list(column_values.value())
            query =f"update {table} SET {set_clause}"
            if filter_condition :
                query += f"{filter_condition}"
            self.cursor.execute(query,values)
            self.db.commit()
            affected_rows = self.cursor.rowcount
            update_status = dict(status ="success", affected_rows=affected_rows)
        except Exception as e:
            error_message = f"Error :{e} while updating {table} for {column_values} with filter condition {filter_condition} "
            raise Exception(error_message)
        return update_status
    
    
    
    
    def insert(self , table_name ,column_values,filter_condition= None):
        insert_status = None
        
        
        try:
            columns = ", ".join(column_values.keys())
            placeholders = ", ".join(["%s"] * len(column_values))
            query = f"INSERT INTO{table_name} ({columns}) VAlUES ({placeholders})"
            data = tuple(column_values.values())
            self.cursor.execute(query,data)
            self.db.commit()
            last_row_id = self.cursor.lastrowid
            insert_status = dict(status ="success",aftected_row=self.cursor.rowcount,last_row_id =last_row_id)
        except Exception as e:
            error_message = f"Error:{e} while inserting {table_name}, filter_condition:{filter_condition}"
            
        return insert_status
    
    
    def delete(self,table,filter_condition= None):
        delete_status = None
        
        try :
            query = f"DELETE FROM {table}"
            if filter_condition:
                query += f"{filter_condition}"
            
            self.cursor.execute(query)
            self.db.commit()
            affected_rows =self.cursor.rowcount
            delete_status = dict(status ="succes",affected_rows=affected_rows)
            return delete_status
        
        except Exception as e:
            error_message = f"Error:{e} while deleting {table} with filter_condition {filter_condition}"
            
        return delete_status
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
   

    
    # def select(self,table_name,columns=None,filter_condition=None):
    #     # update_staus = mysql_client.select(table='product',column_values={'end_date':'31-Dec-24'},filter_condition=f"where first_name ='teddy')
    #     results =[]
    #     select_status =None
    #     try:
    #         if self.db is not None:
    #             if columns is None:
    #                 query =f"SELECT * FROM {table_name}"
    #             else:
    #                 columns_str=','.join(columns)
    #                 query =f"SELECT {columns_str} FROM {table_name}"
    #             if filter_condition:
    #                 query +=f" WHERE {filter_condition}"
    #             self.cursor.execute(query)
    #             rows =self.cursor.fetchall()
    #             results = [dict(zip(self.cursor.column_name,rows)) for row in rows]
    #             select_status = dict(status="success", results = results)
    #                 # return json.dumps(result)
    #         else:
    #             error_message =f"Please make the connection first"
    #             raise ConnectionError(error_message)
            
    #     except Exception as e:
    #         error_message = f"Failed to execute"
    #         print(error_message)
            
    #         raise ConnectionError(error_message)
    #     return select_status
    
    
   
    
    
    # def insert():
    #     pass
            
        
            
            
            
#########################################################################################################
    # def __init__(self,mysql_uri) -> None:
    #     self.mysql_uri =mysql_uri
    #     try:
    #         # mysql_uri = "mysql://myuser:mypassword@localhost:3306/mydatabase"
    #         self.con=mysql.connector.connect(host="localhost",user="root",password="ayush",database="employees")
    #         self.cur= self.con.cursor(dictionary=True)
    #         print("Connection Scccesful")
        
    #     except:
    #         print("error genertaion")
            
            
    # def get(self):
    #     self.cur.execute("SELECT * FROM  employees")
    #     result =self.cur.fetchall()
    #     # print(result)
    #     if len(result)>0:
    #         return json.dumps(result,default=self.json_serial)
    #     else:
    #         return "not data found"
    
    # @staticmethod
    # def json_serial(obj):
    #     """JSON serializer for objects not serializable by default json code"""
    #     if isinstance(obj, date):
    #         return obj.isoformat()
    #     raise TypeError(f"Type {type(obj)} not serializable")
        
        
    # def post(self,data):
    #     self.cur.execute(f"SELECT  * FROM employees ")
    
    
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
                    
                    
        
        
        
    
           
        #    if len(db)>0:
        #        return "Database connection created successfully!"
        #    else:
        #        error_mesaage =f"Database connection created suceesful"
        #        raise ConnectionError(error_mesaage)
        # except 
           
    
    
    
    
    
    
    
    