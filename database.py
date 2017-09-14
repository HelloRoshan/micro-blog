import pymongo

class Database(object): # database is an object and defines additional properties
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod # not only for 1 but for many so no self and tells willl not use self
    def intialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['blog']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)