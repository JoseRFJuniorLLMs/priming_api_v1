# Priming API

## Endpoints

### STUDENT

GET /student/{username}

- Retrieve information about a student based on the provided username.

POST /student/

- Create a new student. The request body should include the necessary student fields.

DELETE /student/{username}

- Delete a student based on the provided username.

PATCH /student/{username}

- Edit a student's information. The request body should include the updated student fields.

### LOGIN

GET '/' 

- Initial endpoint for receiving a welcome message

POST /login

- Authenticate a user by providing the username and password in the request body.

GET /logout

- Terminate the user session and log out.

GET /auth

- Endpoint for Google login.

### LESSONS

GET /lessonDone/student/{student_id}

- Retrieve lessons completed by a student based on the provided student ID.

GET /lesson/course/{course_id}

- Retrieve lessons based on the provided course ID.

GET /lesson/{lesson_id}

- Retrieve information about a specific lesson based on the provided lesson ID.

## Running the Project
### To run the project, follow these steps:

Install Docker Compose.

Execute the Docker Compose command to set up the environment and install dependencies.

- docker-compose up

This will initialize the Priming API and make it accessible.

Feel free to explore the various endpoints to manage student data, perform authentication, 
and retrieve lesson information. If you encounter any issues or have questions, 
please refer to the project documentation or contact the project maintainers.