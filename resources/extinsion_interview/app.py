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
    
    # slicing
    banner("Spliting audio")
    
    list_paths = sliceAudio(path=path)
        
    banner('Done')
    # list_paths = [50,57,45]
    # print(list_paths)
    
    banner("converting audio to txt")
    # givenAnsDB = []
    # for i in range(0,len(list_paths)):
        
    givenAnsDB = convertText(list_paths)
        
    # givenAnsDB.append(text)
        
    # print(givenAnsDB)
    
    banner("Done") if len(givenAnsDB) == len(list_paths) else banner("Fatal error : Can't convert given part of audio")
    
    # for j in range(len(givenAnsDB)):
        
    #     print(f"Result {j} :",givenAnsDB[j])
        
    while True:
        
        try:
            banner("Getting answers")
            answerDB = []
            questionsDB = ["what is machine learning","what is artificial intelligence","what is data science","what is data structure","what is deep learning"]
            # questionsDB = ["what is machine learning","what is data science","what is data structure"]

            for i in range(0,len(questionsDB)):
                
                temp_list = getAnswers(questionsDB[i])
                answerDB.append(temp_list)
            print(answerDB) 
    
            break # break out of the while loop if the try block is successful
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
    
    for k in range(0,(len(answerDB))-2):
        temp = getScore(answerDB[k],givenAnsDB[k])
        ansScores.append(temp)
        # print(givenAnsDB[k])
    print(ansScores)
    total = 0
    for l in range(0,len(ansScores)):
        total += ansScores[l]
        
    totalScore = total/len(ansScores)
    print(totalScore,"\n")
    # Open the file in write mode
    # file = open(r'D:\Projects and codes\interview\resources\extinsion_interview\result.txt', 'w')

    # file.write(f'{totalScore}')
    # # 

    # file.close()

    # Create a Python dictionary
    # data = {"Result 1": ansScores[0],"Result 2": ansScores[1],"Result 3": ansScores[2]}
    data = {"Results": [{"Question":"What is Ml","Result": ansScores[0]},{"Question":"What is AI","Result": ansScores[1]},{"Question":"What is Data Science","Result": ansScores[2]},{"Question":"What is Data Structures","Result": ansScores[2]},{"Question":"What is Deepleaning","Result": ansScores[2]}]}
    writeData(data)         
    banner("completed execution")
    

if __name__ == "__main__":
    # print("in if")
    main()
    