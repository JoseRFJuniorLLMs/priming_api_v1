Priming

Login
POST https://priming-1532995a3138.herokuapp.com/login
https://priming-1532995a3138.herokuapp.com/login
{
    "username": "fred",
    "password": "fred"
}
//"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmcmVkIiwiZXhwIjoxNzExOTk5NDQ0fQ.SfImiHFoHPlpnY6OP0ud5D9aMKP0q_OvuNYdZFfwebg",
//"token_type": "bearer"



https://priming-1532995a3138.herokuapp.com/login
{
    "username": "fritz",
    "password": "fritz"
}
//  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmcml0eiIsImV4cCI6MTcxMTk5OTQxN30.mqwnY2FIQolv_eZMj3HdeiJFuTRL4P6v4NBIA6u8MR0",
//  "token_type": "bearer"



LessonDone Student
GET https://priming-1532995a3138.herokuapp.com/lessonDone/student/{student_id} Rota para pegar as liçoes de um studant
https://priming-1532995a3138.herokuapp.com/lessonDone/student/65c6b529c2c6b863b27a3172
https://priming-1532995a3138.herokuapp.com/lessonDone/student/65cc65f4c2c6b863b2e0c93c
https://priming-1532995a3138.herokuapp.com/lessonDone/student/65cc662ac2c6b863b2e0cf75
https://priming-1532995a3138.herokuapp.com/lessonDone/student/65db9eb76c70fa175a65a2d0

Lesson Course
GET https://priming-1532995a3138.herokuapp.com/lesson/course/{course_id} Rota para pegar as lições de um curso
https://priming-1532995a3138.herokuapp.com/lesson/course/65c5d833c2c6b863b26ae1df
https://priming-1532995a3138.herokuapp.com/lesson/course/65c5d833c2c6b863b26ae1e0
https://priming-1532995a3138.herokuapp.com/lesson/course/65c5d833c2c6b863b26ae1e1
https://priming-1532995a3138.herokuapp.com/lesson/course/65c5d833c2c6b863b26ae1e2
https://priming-1532995a3138.herokuapp.com/lesson/course/65c5d833c2c6b863b26ae1e3

Lesson Lesson
GET https://priming-1532995a3138.herokuapp.com/lesson/{lesson_id} Rota para pegar os detalhes de uma lição
https://priming-1532995a3138.herokuapp.com/lesson/65cc56a8c542c2f2b54f336e
https://priming-1532995a3138.herokuapp.com/lesson/65cc56aac542c2f2b54f336f


