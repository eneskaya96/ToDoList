from flask import Flask, render_template, url_for, request, redirect ,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db=SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    tableName = db.Column(db.String(200) , default="TODO")
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<Task %r>' %self.id

class TodoTask(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    taskId = db.Column(db.Integer )
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<TODO Task %r>' %self.taskId


class InProgressTask(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    taskId = db.Column(db.Integer )
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<In Progress Task %r>' %self.taskId

class DoneTask(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    taskId = db.Column(db.Integer )
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<Done Task %r>' %self.taskId



@app.route('/', methods=['POST' ,'GET'])
def index():

    if request.method == 'GET':
        tasks = Task.query.order_by(Task.id).all()
        all_tasks = [{'id':task.id,'content':task.content, 'tableName':task.tableName } for task in tasks]
        return jsonify(all_tasks)
 
    else:
        pass
        




@app.route('/createTask', methods=['POST' ,'GET'])
def createTask():

    if request.method == 'POST':

        data = request.get_json()
        new_task=Task(content=data["content"], tableName="TODO") 
        
        try:
            db.session.add(new_task)
            db.session.commit()

            todo_task=TodoTask(taskId=new_task.id,content=new_task.content)
            db.session.add(todo_task)
            db.session.commit()
            return jsonify(result = "SUCCESS")

        except:
            return jsonify(result = "ERROR - create new task error")
    else:
        pass


@app.route('/getTasks/<string:table>', methods=['POST' ,'GET'])
def getTasks(table):

    if request.method == 'GET':
        if table == "TODO":
            tasks = TodoTask.query.order_by(TodoTask.id).all()
        elif table == "INPROGRESS":
            tasks = InProgressTask.query.order_by(InProgressTask.id).all()
        elif table == "DONE":
            tasks = DoneTask.query.order_by(DoneTask.id).all()
        
        
        all_tasks = [{'content':task.content,'id':task.taskId} for task in tasks]
        return jsonify(all_tasks)
    else:
        pass




@app.route('/moveTask/<int:id>/<string:toTable>', methods=['POST' ,'GET'])
def moveTask(id,toTable):

    if request.method == 'GET':
        task_get =Task.query.get_or_404(id)
        
        
        try:
            
            if task_get.tableName == "TODO":
                task_remove = TodoTask.query.filter_by(taskId=task_get.id).first()
            elif task_get.tableName == "INPROGRESS":
                task_remove =InProgressTask.query.filter_by(taskId=task_get.id).first()
            elif task_get.tableName == "DONE":
                task_remove =DoneTask.query.filter_by(taskId=task_get.id).first()

            
            
            #delete old table
            db.session.delete(task_remove)
            db.session.commit()
            
            
            #add to new table
            try:
                if toTable == "TODO":
                    task_add =TodoTask(taskId=task_get.id,content=task_get.content)
                elif toTable == "INPROGRESS":
                    task_add =InProgressTask(taskId=task_get.id,content=task_get.content)
                elif toTable == "DONE":
                    task_add =DoneTask(taskId=task_get.id,content=task_get.content)

                db.session.add(task_add)
                db.session.commit()


                # change Task Table
                try:
                    task_get.tableName = toTable
                    db.session.commit()
                    return jsonify(result = "SUCCESS")
                except: 
                    return jsonify(result = "ERROR - task table change error")

            except: 
                return jsonify(result = "ERROR - add task to new table error")

            
        except:
            return jsonify(result = "ERROR - delete task from old table error")
    else:
        pass


if __name__ == "__main__":
    app.run(debug=True)