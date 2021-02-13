from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#all TASKs table
class Task(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    tableName = db.Column(db.String(200) , default="TODO")
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<Task %r>' %self.id

#all TODO TASKs table
class TodoTask(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    taskId = db.Column(db.Integer )
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<TODO Task %r>' %self.taskId

#all InProgress TASKs table
class InProgressTask(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    taskId = db.Column(db.Integer )
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<In Progress Task %r>' %self.taskId

#all Done TASKs table
class DoneTask(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    taskId = db.Column(db.Integer )
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<Done Task %r>' %self.taskId