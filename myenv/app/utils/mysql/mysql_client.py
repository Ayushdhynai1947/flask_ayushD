import mysql.connector
from flask.views import MethodView







class MySQLClient():
    
    # def __init__(self,) -> None:
    #     try:
            # mysql_uri = "mysql://myuser:mypassword@localhost:3306/mydatabase"
    #         self.con=mysql.connector.connect(host="localhost",user="root",password="ayush",database="employee")
    #         self.cur= self.con.cursor(dictionary=True)
    #         print("Connection Scccesful")
        
    #     except:
    #         print("error genertaion")
        
        
        
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
           
           if db:
               db =
           
    
    
    
    
    
    
    
    