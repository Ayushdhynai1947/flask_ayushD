from flask_restful import Resource
from app.utils.mysql.mysql_client import MySQLClient
from app.utils.config.config_client import ConfigClient
from app.utils.csv.csv_client import CsvClient


class CsvResouce(Resource):
    def get(self):
        try:
            config = ConfigClient(env="dev")
            mysql_uri = config.get_value("Database","uri")
            mysql_client = MySQLClient(mysql_uri)
            csv_client = CsvClient()
            issue_date = csv_client.read()
            for row in issue_date:
                print(f"Execuitng for{row}")
                
                # # selecting your table name
                # table_name = ''
                
                # #ensue columns are correct extracted 
                # columns = list(row.key(email))
                # email  = row['email']
                
                # #filter condition
                # filter_condition =f'email = davesmith@bogusemail.com '
                
                # insert_status =mysql_client.insert(table_name='',column_values =row)
                insert_status = mysql_client.select(table_name='', columns='*', filter_condition=f"email = maryjacobs@bogusemail.com")
                
                # insert_status = mysql_client.select(table_name='product',columns='', filter_condition=f" email = 'maryjacobs@bogusemail.com'")
                print(f"Select Status: {insert_status}")
            # return {'message':row}
            return {'message':issue_date}
        
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            return {'error': error_message}, 500
        
    def post(self):
        return {'message':'post request received'}
        