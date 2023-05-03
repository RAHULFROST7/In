import pymongo

connection_string = "mongodb+srv://interview:12345@cluster0.1ahe7l7.mongodb.net/interview?retryWrites=true&w=majority"
database_name = "interview"
collection_name = "questions"

# create a MongoClient object and connect to your MongoDB instance
client = pymongo.MongoClient(connection_string)

# get the database
db = client[database_name]

# get the collection
collection = db[collection_name]

# you can now perform operations on the collection
# for example, find all documents in the collection

# fetch all documents from the collection
docs = collection.find()

# print each document
for doc in docs:
    data = (doc['ques'])
print(data)