<<<<<<< HEAD
from pymongo import MongoClient

def answers(question):
    client = MongoClient('mongodb+srv://webinterview:12345@cluster0.unj3vql.mongodb.net/main?retryWrites=true&w=majority')
    # print('connection successful');

    db = client['main']
    col = db['questions']

    myquery = {'question':question}

    data = col.find(myquery)

    for i in data:
        collected = list(i.values())[1:]
=======
from pymongo import MongoClient

def answers(question):
    client = MongoClient('mongodb+srv://webinterview:12345@cluster0.unj3vql.mongodb.net/main?retryWrites=true&w=majority')
    # print('connection successful');

    db = client['main']
    col = db['questions']

    myquery = {'question':question}

    data = col.find(myquery)

    for i in data:
        collected = list(i.values())[1:]
>>>>>>> 06df0b248b9478cffc78e50b274d2b4cb69cf689
    return collected