from typing import Any

from flask import jsonify, request

from resources.database.db import db


class Task:

    def __init__(self):
        self.db = db  # Use the database instance from the imported `db`

    def findAll(self):
        self.db.db_cursor.execute("SELECT * FROM tasks")
        tasks = db.db_cursor.fetchall()

        return {"status": 200, "message": "Tasks fetch successful", "tasks": tasks}

    def deleteOne(self, task_id):
        print({task_id})
        try:
            self.db.db_cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            self.db.db_connection.commit()

            return jsonify({"status": 200, "message": "Task deleted successfully!"})

        except Exception as e:
            return jsonify(
                {"status": 500, "message": "An error occured", "error": str(e)}
            )

    def updateOne(self, task_id):

        print({task_id})

        try:
            content_type = request.headers.get("Content-Type", "").lower()
            title = None
            description = None
            completed = None

            if "application/json" in content_type:
                data = request.get_json()
                title = data.get("title")
                description = data.get("description", "")
                completed = data.get("completed")

            elif "application/x-www-form-urlencoded" in content_type:
                title = request.form.get("title")
                description = request.form.get("description")
                completed = request.form.get("completed")
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

            # Build the query dynamically based on provided data
            fields_to_update = []
            values = []

            if title is not None:
                fields_to_update.append("title = ?")
                values.append(title)

            if description is not None:
                fields_to_update.append("description = ?")
                values.append(description)

            if completed is not None:
                fields_to_update.append("completed = ?")
                values.append(bool(int(completed)))  # Ensure boolean type

            if not fields_to_update:
                return (
                    jsonify({"status": 400, "message": "No fields to update provided"}),
                    400,
                )

            query = f"UPDATE tasks SET {', '.join(fields_to_update)} WHERE id = ?"
            values.append(task_id)

            self.db.db_cursor.execute(query, values)
            self.db.db_connection.commit()

            return jsonify({"status": 200, "message": "Task updated successfully!"})

        except Exception as e:
            return jsonify(
                {"status": 500, "message": "An error occurred", "error": str(e)}
            )

    def store(self):

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

            self.db.db_cursor.execute(
                "INSERT INTO tasks (title, description) VALUES (?, ?)",
                (title, description),
            )

            self.db.db_connection.commit()
            print("To do task successfully added")

            return {"status": 200, "message": "Tasks added successfully"}

        except Exception as e:
            return {"status": 500, "message": "An error occured", "error": str(e)}
