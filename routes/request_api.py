from flask import request, jsonify, Blueprint
from models import db
from models import TaskContainer


REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

@REQUEST_API.route('/static/<path:path>')
def get_static():
    return


# when enter index.html get all tasks
@REQUEST_API.route('/tasks/getAllTasks', methods=['POST', 'GET'])
def get_all_tasks():
    if request.method == 'GET':
        Tasks = TaskContainer.query.order_by(TaskContainer.id).all()
        AllTasks = [{'id': Task.id, 'content': Task.content, 'table_name': Task.table_name} for Task in Tasks]
        return jsonify(AllTasks)

    else:
        pass

# get specific table tasks like TODO,INPROGRESS,DONE
@REQUEST_API.route('/tasks/getTasks/<string:table>', methods=['POST', 'GET'])
def get_tasks(table):
    if request.method == 'GET':
        tasks = TaskContainer.query.filter_by(table_name=table).all()
        all_tasks = [{'content': task.content, 'id': task.id} for task in tasks]
        return jsonify(all_tasks)
    else:
        pass

# create task with content parameter
@REQUEST_API.route('/task/createTask', methods=['POST', 'GET'])
def create_task():
    if request.method == 'POST':

        Data = request.get_json()
        new_task = TaskContainer(content=Data["content"], table_name="TODO")

        try:
            db.session.add(new_task)
            db.session.commit()

            return jsonify(result="SUCCESS")
        except:
            return jsonify(result="ERROR - create new task error")
    else:
        pass

# move to task from one table to another with taks is
@REQUEST_API.route('/task/moveTask/<int:id>/<string:to_table>', methods=['POST', 'GET'])
def move_task(id, to_table):
    if request.method == 'GET':
        task_get = TaskContainer.query.get_or_404(id)

        try:
            task_get.table_name = to_table
            db.session.commit()
            return jsonify(result="SUCCESS")
        except:
            return jsonify(result="ERROR - can not moved")
    else:
        pass