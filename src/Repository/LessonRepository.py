from src.Repository.Repository import connection
from bson import ObjectId


class LessonRepository:
    @staticmethod
    def get_lessons_by_course(course_id):
        db = connection()

        course_id =  ObjectId(course_id)

        # Agregação para unir as coleções e buscar os documentos das lições
        pipeline = [
            {'$match': {'_id': course_id}},
            {'$lookup': {
                'from': 'LessonCollection',
                'localField': 'lessons',
                'foreignField': '_id',
                'as': 'lesson_details'
            }},
            {'$unwind': '$lesson_details'},
            {'$project': {
                '_id': 0,
                'lesson_id': '$lesson_details._id',
                'course_name': '$name',
                'lesson_name': '$lesson_details.name',
                'lesson_description': '$lesson_details.description'
            }}
        ]

        return list(db.CourseCollection.aggregate(pipeline))

    @staticmethod
    def get_lesson_by_id(lesson_id):
        db = connection()
        lesson_id = ObjectId(lesson_id)
        pipeline = [
            {'$match': {'_id': lesson_id}},
            {'$lookup': {
                'from': 'LessonCollection',
                'localField': '_id',
                'foreignField': '_id',
                'as': 'lesson_details'
            }},
            {'$lookup': {
                'from': 'primeCollection',
                'localField': 'lesson_details.prime',
                'foreignField': '_id',
                'as': 'prime_details'
            }},
            {'$lookup': {
                'from': 'primeTargetDictionaryCollection',
                'localField': 'lesson_details.dictionary',
                'foreignField': '_id',
                'as': 'dictionary_details'
            }},
            {'$lookup': {
                'from': 'primeTargetYoutubeCollection',
                'localField': 'lesson_details.youtubeUrl',
                'foreignField': '_id',
                'as': 'youtube_details'
            }},
            {'$lookup': {
                'from': 'primeTargetTextCollection',
                'localField': 'lesson_details.text',
                'foreignField': '_id',
                'as': 'text_details'
            }},
            {'$lookup': {
                'from': 'primeTargetPhraseCollection',
                'localField': 'lesson_details.phrase',
                'foreignField': '_id',
                'as': 'phrase_details'
            }},
            {'$unwind': '$lesson_details'},
            {'$unwind': '$prime_details'},
            {'$unwind': '$youtube_details'},
            {'$unwind': '$text_details'},
            {'$unwind': '$phrase_details'},
            {'$unwind': '$dictionary_details'},
            {'$project': {
                '_id': 0,
                'lesson_id': '$lesson_details._id',
                'lesson_name': '$lesson_details.name',
                'prime': '$prime_details.prime',
                'text': '$text_details.text',
                'youtube_link': '$youtube_details.url',
                'phrases': '$phrase_details.phrase',
                'dictionary': '$dictionary_details.text'
            }}
        ]

        return list(db.LessonCollection.aggregate(pipeline))
