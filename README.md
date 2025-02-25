# SCSU Student API

This is a FastAPI-based CRUD API for managing student records. The API uses SQLite for database storage and provides endpoints for creating, reading, updating, and deleting student records. It also includes a simple frontend to interact with the API.

## Features
- Create a new student record
- Retrieve student details
- Update an existing student record
- Delete a student record
- Swagger documentation enabled by default
- SQLite database for persistence

## Technologies Used
- FastAPI
- SQLite
- SQLAlchemy
- Uvicorn
- HTML, JavaScript (for frontend)

## Installation
### Prerequisites
- Python 3.7+
- pip installed

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/scsu-student-api.git
   cd scsu-student-api
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```
5. Open Swagger UI in your browser:
   ```
   http://127.0.0.1:8000/docs
   ```

## API Endpoints
| Method | Endpoint | Description |
|--------|------------|----------------------|
| POST   | `/students` | Create a new student |
| GET    | `/students/{id}` | Retrieve student details |
| GET    | `/students` | Retrieve all students |
| PUT    | `/students/{id}` | Update a student record |
| DELETE | `/students/{id}` | Delete a student record |

## Frontend
A simple frontend is provided in `index.html`. Open it in a browser and ensure the API server is running to interact with student records.

## Troubleshooting
- If you get a `405 Method Not Allowed` error, ensure the correct endpoint and method are used.
- If you get CORS issues, ensure the middleware is properly configured.

## License
This project is licensed under the MIT License.

## Author
Ashesh Nepal - [GitHub Profile](https://github.com/ashesh808)

