# list_word_done_repository.py

from bson import ObjectId
import datetime
from Model.WordLearningInfo import WordLearningInfo
from Model.ListWordDone import ListWordDone
"""
Lógica: O sistema de revisão espaçada (SRS) foi criado por Piotr Wozniak
    Obtém a data e hora atuais.
    Calcula pontos no futuro para as próximas revisões: 1 hora depois, 1 dia depois, 1 semana depois e 1 mês (aproximado) depois.
    Cria um objeto WordLearningInfo contendo:
    A palavra
    Hora da revisão atual (last_reviewed)
    Hora da próxima revisão (next_review) - uma das possíveis datas calculadas
    O nível de dificuldade atual.
    Salva (provavelmente insere ou atualiza) as informações da palavra (WordLearningInfo) no banco de dados.
"""
class ListWordDoneRepository:
    @staticmethod
    async def find_by_student(student_id: ObjectId):
        return await ListWordDone.find_one({"student": student_id})

    @staticmethod
    async def schedule_review(word: str, student_id: ObjectId, difficulty: int):
        now = datetime.datetime.now()
        next_hour = now + datetime.timedelta(hours=1)
        next_day = now + datetime.timedelta(days=1)
        next_week = now + datetime.timedelta(weeks=1)
        next_month = now + datetime.timedelta(days=30)  # Simplificação de 1 mês

        for next_review_time in [next_hour, next_day, next_week, next_month]:
            word_info = WordLearningInfo(
                word=word, last_reviewed=now, next_review=next_review_time, difficulty=difficulty
            )
            await word_info.insert()
