from flask import Flask

from resources.controllers.task.index import Task
from resources.database.db import DatabaseConnection

app = Flask(__name__)

task = Task()
db = DatabaseConnection()


@app.route("/", methods=["GET"])
def home():
    return f"Welcome to To Do List API"


@app.route("/api/v1/all", methods=["GET"])
def index():
    return task.findAll()


@app.route("/api/v1/store", methods=["POST"])
def create():
    return task.store()


@app.route("/api/v1/delete/<int:task_id>", methods=["DELETE"])
def remove(task_id):
    return task.deleteOne(task_id)


@app.route("/api/v1/update/<int:task_id>", methods=["PATCH"])
def update(task_id):
    return task.updateOne(task_id)


if __name__ == "__main__":
    db.db_init()

    app.run(debug=True)
