from src.Repository.Repository import connection


class StudentRepository:
    @staticmethod
    def validate_login(username: str, password: str):
        db = connection()
        query = {"login": username, "password": password}

        student = db.StudentCollection.find(query)
        for student in student:
            student = student
        return student

    @staticmethod
    def get_student_by_login(login: str) -> dict:
        db = connection()
        query = {"login": login}

        student = db.StudentCollection.find_one(query)
        return student
