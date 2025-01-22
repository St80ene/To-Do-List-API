from flask import Flask, jsonify, request

from database.db import db_init
from src.controllers.task.index import findAll, store

app = Flask(__name__)


@app.route("/")
def home():
    return f"Welcome to To Do List API"


@app.route("/all")
def viewAll():
    return findAll()


@app.route("/store", methods=["POST"])
def create():
    store()


if __name__ == "__main__":
    db_init()

    app.run(debug=True)
