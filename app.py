from flask import Flask

from resources.controllers.task.index import Task
from resources.database.db import DatabaseConnection

app = Flask(__name__)

task = Task()
db = DatabaseConnection()


@app.route("/")
def home():
    return f"Welcome to To Do List API"


@app.route("/all")
def viewAll():
    return task.findAll


@app.route("/store", methods=["POST"])
def create():
    task.store()


@app.route("/delete<int: task_id>", methods=["DELETE"])
def create():
    task.store()


@app.route("/update<int: task_id>", methods=["PATCH"])
def create():
    task.store()


if __name__ == "__main__":
    db.db_init()

    app.run(debug=True)
