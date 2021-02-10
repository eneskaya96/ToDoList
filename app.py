from flask import Flask, render_template, url_for, request, redirect ,jsonify
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db=SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    tableId = db.Column(db.Integer , default=0)
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<Task %r>' %self.id

class TodoTask(db.Model):
    __tablename__ = 'TODO Tasks'
    taskId = db.Column(db.Integer , primary_key=True)
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<TODO Task %r>' %self.taskId


class InProgressTask(db.Model):
    __tablename__ = 'In Progress Tasks'
    taskId = db.Column(db.Integer , primary_key=True)
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<In Progress Task %r>' %self.taskId

class DoneTask(db.Model):
    __tablename__ = 'DONE Tasks'
    taskId = db.Column(db.Integer , primary_key=True)
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<Done Task %r>' %self.taskId



@app.route('/', methods=['POST' ,'GET'])
def index():

    if request.method == 'POST':
        task_content = request.form['content']
        new_task =Task(content="he")

        try:
            db.session.add(new_task)
            db.session.commit()

        except:
            return "error"
    else:
        tasks = Todo.query.order_by(Todo.id).all()


    return render_template('index.html')


@app.route('/create', methods=['POST' ,'GET'])
def create():

    if request.method == 'POST':

        data = request.get_json()
        new_task=Task(content=data["content"]) #

        try:
            db.session.add(new_task)
            db.session.commit()
            return "The task with id = %d is added" %new_task.id

        except:
            return "The task can not be added %s" %data["content"]
    else:
        pass


@app.route('/get/<int:id>', methods=['POST' ,'GET'])
def get(id):

    if request.method == 'GET':
        task_get =Task.query.get_or_404(id)
            
        return  jsonify(content=task_get.content) 
    else:
        pass


if __name__ == "__main__":
    app.run(debug=True)