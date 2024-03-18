# API Documentation

## Overview
This API is designed to manage a learning platform. It provides endpoints for managing students, courses, lessons, users, phrases, notes, tags, list of words, and more. The API is built with Python and FastAPI.  
## Base URL
The base URL for all the endpoints is: http://localhost:8000  
## Endpoints

### Students
- GET /student/{id}: Retrieves a student by their ID.
- GET /student/: Retrieves all students.
  - Params: name | email
- DELETE /student/{id}: Deletes a student by their ID.

### Courses

- GET /course/{id}: Retrieves a course by its ID.
- GET /course/: Retrieves courses by params or all params.
  - Params: name | level
- POST /course/: Creates a new course.
  - Body: ```{"name": str, "category": str, "level": str, "price": str, "status": str, "objective": str, "content": List[str] | None, "lessons": List[ObjectId] | None}```
- PATCH /course/: Updates a course.
  - Body: ```{"id": ObjectId, "name": str, "category": str, "level": str, "price": str, "status": str, "objective": str, "content": List[str] | None, "lessons": List[ObjectId] | None}```
- DELETE /course/{id}: Deletes a course by its ID.

### Lessons

- GET /lesson/{id}: Retrieves a lesson by its ID.
- GET /lesson/: Retrieves all lessons.
  - Param: name
- POST /lesson/: Creates a new lesson.
  - Body: ```{"name": str, "dictionary": ObjectId | None, "phrase": ObjectId | None, "prime": ObjectId, "text": ObjectId | None, "youtubeUrl": ObjectId | None}```
- PATCH /lesson/: Updates a lesson.
  - Body: ```{"id": ObjectId, "name": str, "dictionary": ObjectId | None, "phrase": ObjectId | None, "prime": ObjectId, "text": ObjectId | None, "youtubeUrl": ObjectId | None}```
- DELETE /lesson/{id}: Deletes a lesson by its ID.

### Users

- POST /login: Make login
  - Body: ```{"email": str, "password": str}```
- POST /user/: Creates a new user.
  - Body: ```{"name": str, "password": str, "login": str, "email": str, "status": str | None, "city": str | None, "country": str | None, "tax_ident_number": str | None, "personal_ident_number": str | None, "date_create": str | None, "facebook": str | None, "x": str | None, "tiktok": str | None, "instagram": str | None, "linkedin": str | None, "phone": str | None, "spoken_language": str | None, "image_url": str | None, "bitcoin": ObjectId | None, "lessons_done": ObjectId | None, "books": ObjectId | None, "courses": ObjectId | None, "scheduled_lessons": ObjectId | None, "list_word_text": ObjectId | None}```
- PATCH /user/: Updates a user.
  - Body: ```{"id": ObjectId, "name": str, "password": str, "login": str, "email": str, "status": str | None, "city": str | None, "country": str | None, "tax_ident_number": str | None, "personal_ident_number": str | None, "date_create": str | None, "facebook": str | None, "x": str | None, "tiktok": str | None, "instagram": str | None, "linkedin": str | None, "phone": str | None, "spoken_language": str | None, "image_url": str | None, "bitcoin": ObjectId | None, "lessons_done": ObjectId | None, "books": ObjectId | None, "courses": ObjectId | None, "scheduled_lessons": ObjectId | None, "list_word_text": ObjectId | None}```

### Phrases

- GET /phrase/{id}: Retrieves a phrase by its ID.
- GET /phrase/: Retrieves all phrases.
  - Param: prime
- POST /phrase/: Creates a new phrase.
  - Body: ```{"prime": str, "target": str, "phrase": List[str], "imagem": List[str] | None, "url": List[str] | None}```
- PATCH /phrase/: Updates a phrase.
  - Body: ```{"id": ObjectId, "prime": str, "target": str, "phrase": List[str], "imagem": List[str] | None, "url": List[str] | None}```
- DELETE /phrase/{id}: Deletes a phrase by its ID.

### Notes

- GET /note/{id}: Retrieves a note by its ID.
- GET /note/: Retrieves all notes.
  - Param: title
- POST /note/: Creates a new note.
  - Body: ```{"title": str, "description": str | None, "student_id": ObjectId, "tags": List[ObjectId] | None}```
- PATCH /note/: Updates a note.
  - Body: ```{"id": ObjectId, "title": str, "description": str | None, "student_id": ObjectId, "tags": List[ObjectId] | None}```
- DELETE /note/{id}: Deletes a note by its ID.

### Tags

- GET /tag/{id}: Retrieves a tag by its ID.
- GET /tag/: Retrieves all tags by student.
  - Param: student_id
- POST /tag/: Creates a new tag.
  - Body: ```{"name": str, "description": str | None, "student_id": ObjectId}```
- PATCH /tag/: Updates a tag.
  - Body: ```{"id": ObjectId, "name": str, "description": str | None, "student_id": ObjectId}```
- DELETE /tag/{id}: Deletes a tag by its ID.

### List of Words

- GET /list-word/{id}: Retrieves a list of words by its ID.
- GET /list-word/: Retrieves all lists of words by prime.
  - Param: prime
- POST /list-word/: Creates a new list of words.
  - Body: ```{"list_word": List[str], "text_prime": ObjectId | None}```
- PATCH /list-word/: Updates a list of words.
  - Body: ```{"id": OjectId, "list_word": List[str], "text_prime": ObjectId | None}```
- DELETE /list-word/{id}: Deletes a list of words by its ID.

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of an API request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the 5xx range indicate an error with the server.  

## Rate Limiting

There is currently no rate limiting for this API.  

## Authentication

This API uses JWT for authentication. To authenticate, you need to include the JWT token in the Authorization header with the Bearer schema.  

## Data Format

The API uses JSON for both requests and responses.