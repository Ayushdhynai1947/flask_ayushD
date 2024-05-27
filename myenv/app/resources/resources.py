from flask_restful import Resource, reqparse, abort, fields, marshal_with
from app.models import USER




resource_fields={
    'emp_no':fields.Integer,
    'product_name':fields.String,
    'first_name':fields.String,
    'last_name':fields.String,
    
}



class Todos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        tasks = USER.query.all()
        return tasks, 200
    

