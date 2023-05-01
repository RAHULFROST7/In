import sys

sys.path.append(r'D:\Projects and codes\interview\resources')


from Transcriber import convertText
from NLP_engine import getScore
from slicer import sliceAudio
from pymongo import MongoClient
from typing import NewType
import json
import time

def banner(text):
    # for loging
    print(f"!! {text} !!\n")
    
def writeData(data):

    # data = {"Result 1": 23, "Result 2": 30, "Result 3": 54}

    # Open a file for writing
    with open(r"resources\extinsion_interview\result.json", "w") as f:
        # Use json.dump() to write the data to the file
        json.dump(data, f)

askedQuestion = NewType('askedQuestion',str)

def getAnswers(question : askedQuestion):
    
    client = MongoClient('mongodb+srv://webinterview:12345@cluster0.unj3vql.mongodb.net/main?retryWrites=true&w=majority')
    # print('connection successful');

    db = client['main']
    col = db['questions']

    myquery = {'question':question}

    data = col.find(myquery)

    for i in data:
        collected = list(i.values())[1:]
        
    return collected[1:]

def main():
    
    
    banner("MAIN")
    
    path = r"D:\Projects and codes\interview\resources\extinsion_interview\out.wav"

    banner("Spliting audio")
    
    list_paths = sliceAudio(path=path)
        
    banner('Done')
    
    banner("converting audio to txt")
        
    givenAnsDB = convertText(list_paths)
        
    # print(givenAnsDB)
    
    banner("Done") if len(givenAnsDB) == len(list_paths) else banner("Fatal error : Can't convert given part of audio")
        
    while True:
        
        try:
            banner("Getting answers")
            answerDB = []
            questionsDB = ["what is machine learning","what is artificial intelligence","what is data science","what is data structure","what is deep learning"]

            for i in range(0,len(questionsDB)):
                
                temp_list = getAnswers(questionsDB[i])
                answerDB.append(temp_list)
            # print(answerDB) 
    
            break 
        except:
            banner("<Network Error>")
            waiting_time = 20
            print(f"Waiting for {waiting_time} seconds...", end='')
            for i in range(waiting_time, -1, -1):
                print(f"\r{i} seconds remaining...{' '*(len(str(waiting_time))-len(str(i)))}", end='')
                time.sleep(1)
            banner("Retrying")
            
    banner("Done")
        

    banner("Comparing for score")
    
    ansScores = []
    
    for k in range(0,(len(answerDB))):
        temp = getScore(answerDB[k],givenAnsDB[k])
        ansScores.append(temp)
        # print(givenAnsDB[k])
    print(ansScores)
    total = 0
    for l in range(0,len(ansScores)):
        total += ansScores[l]
        
    totalScore = total/len(ansScores)
    print(f"\n{totalScore}\n")

    data = {"results": [{"question":"What is Ml","result": ansScores[0]},{"question":"What is AI","result": ansScores[1]},{"question":"What is Data Science","result": ansScores[2]},{"question":"What is Data Structures","result": ansScores[3]},{"question":"What is Deepleaning","result": ansScores[4]}]}
    writeData(data)         
    banner("completed execution")
    

if __name__ == "__main__":

    main()
    