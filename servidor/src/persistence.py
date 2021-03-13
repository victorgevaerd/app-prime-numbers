from pickle import load, dump


class PrimeRecord:
    def __init__(self, number_one: int, number_two: int):
        self.__number_one = number_one
        self.__number_two = number_two

    @property
    def number_one(self):
        return self.__number_one

    @property
    def number_two(self):
        return self.__number_two


class PrimesDAO:
    def __init__(self):
        self.__data_source = '.\primes.pkl'
        self.__object_cache = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def __load(self):
        self.__object_cache = load(open(self.__data_source, 'rb'))

    def __dump(self):
        dump(self.__object_cache, open(self.__data_source, 'wb'))

    def add(self, prime_record):
        if isinstance(prime_record, PrimeRecord):
            self.__object_cache.append(prime_record)
            self.__dump()
    
    def get_all(self):
        return self.__object_cache
