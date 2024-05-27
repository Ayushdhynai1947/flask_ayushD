

from  flask import Flask
app = Flask(__name__)
if app.config["ENV"]== "prodction":
    app.config.from_object("confi_maid.ProductionConfig")
elif app.config["ENV"]== "testing":
    app.config.from_object("confi_maid.TestingConfigConfig")
else:
    app.config.from_object("confi_maid.DevelopmentConfig")
