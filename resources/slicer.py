import pymongo
import datetime
from pydub import AudioSegment
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

audio = AudioSegment.from_wav("./resources/out.wav")

print(timestamps)

start_time = 0

for i, duration in enumerate(timestamps):
    end_time = start_time + duration
   
    
    sliced_audio = audio[start_time * 1000:end_time * 1000]

     # Export the sliced audio to a file
    sliced_audio.export(f"./resources/sliced_audio_{i}.mp3", format="mp3")

    start_time = end_time
