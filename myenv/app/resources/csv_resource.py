from flask_restful import Resource
from app.utils.mysql.mysql_client import MySQLClient
from app.utils.config.config_client import ConfigClient
from app.utils.csv.csv_client import CsvClient


class CsvResouce(Resource):
    def get(self):
        config =ConfigClient(env="dev")
        mysql_uri =config.get_value("Database","uri")
        mysql_client =MySQLClient(mysql_uri)
        csv_client =CsvClient()
        issue_date = csv_client.read()
        for row in issue_date:
            print(f"Execuitng for{row}")
            isert_status =mysql_client.insert(table_name='product',column_value =row)
            return {'message':issue_date}
        
    def post(self):
        return {'message':'post request received'}
        