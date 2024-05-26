import mysql.connector







class MySQLClient:
    
    def __init__(self,mysql_uri) -> None:
        self.mysql_uri=mysql_uri
        