# To-Do List API

A simple RESTful API built with Python for managing to-do tasks.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

## Overview

This is a RESTful API for managing a to-do list. It allows users to create, read, update, and delete tasks efficiently.
Ideal for developers looking for a simple task management system to integrate into their projects.

## Features

- Add, update, and delete tasks
- Fetch all tasks or a single task by ID

## Tech Stack

- Python
- Flask (for the RESTful API)
- SQLite (database)

## Installation

1. Clone the repository using SSH:

   ```bash
   git@github.com:St80ene/To-Do-List-API.git
   ```

2. Navigate to the project directory:

   ```bash
   cd To-Do-List-API
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the server, run:

```bash
python app.py
```

## API Endpoints

- `/` **(GET)**

  - Description: Displays a welcome message.

- `/api/v1/all` **(GET)**

  - Description: Retrieves a list of all tasks.

- `/api/v1/store` **(POST)**

  - Description: Creates a new task.
  - Request Body:
    - title (string, required): Title of the task.
    - description (string, optional): Description of the task.

- `/api/v1/update/:id` **(PATCH)**

  - Description: Updates an existing task.
  - Path Parameters:
    - `:id` (integer): Unique identifier of the task.
  - Request Body:
    - title (string, optional): New title of the task.
    - description (string, optional): New description of the task.
    - completed (boolean, optional): Indicates whether the task is completed (true) or not (false).

- `/api/v1/delete/:id` **(DELETE)**

  - Description: Deletes a specific task.
  - Path Parameters:
    - `:id` (integer): Unique identifier of the task.

## Technologies Used

- Framework: Flask
- Database: SQLite
- DevOps: Docker
- Other Tools: Git, Postman
