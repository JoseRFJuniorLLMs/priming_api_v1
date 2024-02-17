<<<<<<< HEAD
from Model.DictionaryPrime import DictionaryPrime
=======
from src.Model.DictionaryPrime import DictionaryPrime
>>>>>>> origin/main


class DictionaryPrimeRepository:
    @staticmethod
    async def find_by_prime(prime: str):
        dictionary = await DictionaryPrime.find_one({"prime": prime})
        return dictionary
