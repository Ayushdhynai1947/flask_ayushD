import json

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "dfusdhfdfhdsfiudshf"
    DB_NAME = ""
    DB_USERNAME = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    SQLALCHEMY_DATABASE_URI = ""

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = 'employee'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'ayush'
    DB_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

class TestingConfig(Config):
    TESTING = True
    DB_NAME = "Development-DB"
    DB_USERNAME = ""
    DB_PASSWORD = ""
    DB_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}.db'









































# dev_conf ={
#     "Database":{
#         "uri":" "
#         }
    
# }

# prod_conf ={
    
    
    
# }







# # config.py
# class ConfigClient:
#     def __init__(self):
#         self.database_uri = "sqlite:///mydatabase.db"
#         self.secret_key = "my_secret_key"
#         self.debug = True

#     def __str__(self):
#         return f"Config(database_uri={self.database_uri}, secret_key={self.secret_key}, debug={self.debug})"

# # Singleton instance
# _config_instance = None

# def get_config():
#     global _config_instance
#     if _config_instance is None:
#         _config_instance = Config()
#     return _config_instance



# # import json

# # dev_conf = {
# #     "Database": {
# #         "uri" : ""
# #     },
# #     "ChatGpt" : {
# #         "api-key" : ""
# #     }
# # }

# # prod_conf = {
# #     "Database": {
# #         "uri" : ""
# #     }
# # }

# # class ConfigClient:
# #     def __init__(self, env):
# #         if env == 'dev':
# #             self.config = dev_conf
# #         else:
# #             self.config = prod_conf

# #     def get_value(self, section, key):
# #         if section in self.config and key in self.config[section]:
# #             return self.config[section][key]
# #         else:
#             # return None