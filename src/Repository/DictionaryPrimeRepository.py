from src.Model.DictionaryPrime import DictionaryPrime


class DictionaryPrimeRepository:
    @staticmethod
    async def find_by_prime(prime: str):
        dictionary = await DictionaryPrime.find_one({"prime": prime})
        return dictionary
