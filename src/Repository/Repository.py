from pymongo import MongoClient


def connection():
    try:
        cliente = MongoClient("mongodb+srv://junior:debian23@prime.0zjimdw.mongodb.net/?retryWrites=true&w=majority")
        db = cliente['primeDB']
        return db
    except ConnectionError as e:
        return f'falha na conexão: {e}'
