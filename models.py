from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#keep all tasks
class TaskContainer(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    table_name = db.Column(db.String(200) , default="TODO")
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)

    def __repr__(self):
        return '<Task %r>' %self.id

