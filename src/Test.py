import os
from pymongo import MongoClient

def list_collections():
    try:
        # Conectar ao MongoDB
        client = MongoClient("mongodb+srv://junior:debian23@prime.0zjimdw.mongodb.net/?retryWrites=true&w=majority")
        db = client.get_database("primeDB")
        collection_names = db.list_collection_names()
        if collection_names:
            print("Coleções no banco de dados:")
            for collection_name in collection_names:
                print(collection_name)
        else:
            print("Não há coleções no banco de dados.")
    except Exception as e:
        print(f"Erro ao listar coleções: {e}")

if __name__ == "__main__":
    list_collections()