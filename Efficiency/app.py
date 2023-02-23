from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from urllib.parse import quote_plus


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:mypassword@db/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push() 


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<Task %r>' %self.id

@app.route("/", methods=['GET'])
def index():
    tasks = Todo.query.all()
    count = 0
    for task in tasks:
        if task.completed == 1:
            count += 1

    # print(len(tasks))
    # print(count)

    eff = count/len(tasks) * 100
    print(eff)
    return 'Efficiency of task completion is %.3f percentage' %eff


if __name__ == "__main__":
    app.run(debug=True, port=3001)


