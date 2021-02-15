from flask import Flask, jsonify
from models import db
from decouple import config
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_restful import Resource, Api, fields, marshal_with
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

from models import TaskContainer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')

db.init_app(app)
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='TODO List Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

with app.app_context():
    db.create_all()


class TasksResponseSchema(Schema):
    message = fields.Str(default='Success')


class TaskRequestSchema(Schema):
    content = fields.String(required=True, description="content of task")


class GetAllTaskAPI(MethodResource, Resource):
    @doc(description='Get all tasks.', tags=['Tasks'])
    @marshal_with(TasksResponseSchema)
    def get(self):
        Tasks = TaskContainer.query.order_by(TaskContainer.id).all()
        AllTasks = [{'id': Task.id, 'content': Task.content, 'table_name': Task.table_name} for Task in Tasks]
        return jsonify(AllTasks)

api.add_resource(GetAllTaskAPI, '/tasks/getAllTasks')
docs.register(GetAllTaskAPI)


# get specific table tasks like TODO,INPROGRESS,DONE
class GetTaskAPI(MethodResource, Resource):
    @doc(description='Get specific tasks.', tags=['Tasks'])
    @marshal_with(TasksResponseSchema)
    def get(self, table):
        Tasks = TaskContainer.query.filter_by(table_name=table).all()
        AllTasks = [{'content': Task.content, 'id': Task.id} for Task in Tasks]
        return jsonify(AllTasks)

api.add_resource(GetTaskAPI, '/tasks/getTasks/<string:table>')
docs.register(GetTaskAPI)


# create task with content parameter
class CreateTaskAPI(MethodResource, Resource):
    args = {
        'content': fields.Str(
            required=True,
        ),
    }
    @doc(description='Create  Task with content', tags=['Task'])
    @marshal_with(TasksResponseSchema)
    @use_kwargs(args)
    def post(self,content):
        NewTask = TaskContainer(content=content, table_name="TODO")

        try:
            db.session.add(NewTask)
            db.session.commit()

            return jsonify(result="SUCCESS")
        except:
            return jsonify(result="ERROR - create new task error")

api.add_resource(CreateTaskAPI, '/task/createTask')
docs.register(CreateTaskAPI)


# move to task from one table to another with taks is
class MoveTaskAPI(MethodResource, Resource):
    @doc(description='Move Task with id  to toTable', tags=['Task'])
    @marshal_with(TasksResponseSchema)
    def get(self, id, to_table):
        TaskGet = TaskContainer.query.get_or_404(id)
        try:
            TaskGet.table_name = to_table
            db.session.commit()
            return jsonify(result="SUCCESS")
        except:
            return jsonify(result="ERROR - can not moved")


api.add_resource(MoveTaskAPI, '/task/moveTask/<int:id>/<string:to_table>')
docs.register(MoveTaskAPI)

if __name__ == "__main__":
    app.run(debug=True)
