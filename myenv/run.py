from flask import Flask
from flask_restful import Api

from app import create_app


#create an instance of big class





app =create_app()





if __name__=='__main__':
    app.run(debug=True)