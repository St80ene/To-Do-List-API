# To-Do List API 
A simple RESTful API built with Python for managing to-do tasks.


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)


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

### 8. **Usage**

To start the server, run:

```bash
python app.py
```
### 8. **API Endpoints**

GET `/all` - Retrieve all tasks

POST `/store` - Add a new task
  - Body Parameters:
      - title: (string) Task title
      - description: (string) Task description
   

### 9. **Contributing**

Contributions are welcome! Submit a pull request after forking and branching.
