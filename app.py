from flask import Flask, jsonify, request

from database.db import db_connection, db_cursor, db_init

app = Flask(__name__)


@app.route("/")
def home():
    return f"Welcome to To Do List API"


@app.route("/all")
def findOne():
    db_cursor.execute("SELECT * FROM tasks")
    tasks = db_cursor.fetchall()

    return {"status": 200, "message": "Tasks fetch successful", "tasks": tasks}


@app.route("/store", methods=["POST"])
def store():

    try:

        # Check the Content-Type header
        content_type = request.headers.get("Content-Type", "").lower()

        title = ("",)
        description = ""

        # Parse data based on Content-Type
        if "application/json" in content_type:
            data = request.get_json()
            title = data.get("title")
            description = data.get("description", "")

        elif "application/x-www-form-urlencoded" in content_type:
            title = request.form.get("title")
            description = request.form.get("description", "")
            print("2nd: ==>", title, description)
        else:
            return (
                jsonify(
                    {
                        "status": 415,
                        "message": "Unsupported Media Type. Use 'application/json' or 'application/x-www-form-urlencoded'.",
                    }
                ),
                415,
            )

        # Validate input
        if not title:
            return jsonify({"status": 400, "message": "Title is required"}), 400

        print(title, description)
        task = db_cursor.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description),
        )

        db_connection.commit()
        print("To do task successfully added")

        return {"status": 200, "message": "Tasks added successfully"}
    except Exception as e:
        return {"status": 500, "message": "An error occured", "error": str(e)}


if __name__ == "__main__":
    db_init()

    app.run(debug=True)
