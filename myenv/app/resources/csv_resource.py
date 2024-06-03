from flask_restful import Resource
from app.utils.mysql.mysql_client import MySQLClient
from app.utils.config.config_client import ConfigClient
from app.utils.csv.csv_client import CsvClient


class CsvResouce(Resource):
    def get(self):
        config =ConfigClient(env="dev")
        mysql_uri =config.get_value("Database","uri")
        mysql_client =MySQLClient(mysql_uri)
        