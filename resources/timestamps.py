import pymongo
import datetime

# replace the connection string and database/collection names with your own values
connection_string = "mongodb+srv://interview:12345@cluster0.1ahe7l7.mongodb.net/interview?retryWrites=true&w=majority"
database_name = "interview"
collection_name = "timestamps"

# create a MongoClient object and connect to your MongoDB instance
client = pymongo.MongoClient(connection_string)

# get the database
db = client[database_name]

# get the collection
collection = db[collection_name]

# you can now perform operations on the collection
# for example, find all documents in the collection
num_documents = collection.count_documents({})
# for document in collection.find():
#     print(document['start'])
    # timestamp1 = datetime.datetime.strptime(timestamp1_str, "%Y-%m-%d %H:%M:%S")
    # timestamp2 = datetime.datetime.strptime(timestamp2_str, "%Y-%m-%d %H:%M:%S")
timestamps=[]
for i in range(num_documents):
    timestamp1_str = collection.find()[i]['start']
    timestamp2_str = collection.find()[i]['end']
    timestamp1 = datetime.datetime.strptime(timestamp1_str, "%Y-%m-%d %H:%M:%S")
    timestamp2 = datetime.datetime.strptime(timestamp2_str, "%Y-%m-%d %H:%M:%S")
    time_diff = timestamp1 - timestamp2
    timestamps.append(int(abs( time_diff.total_seconds())))
print(timestamps)
    
    