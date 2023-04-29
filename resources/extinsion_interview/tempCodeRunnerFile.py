import sys

sys.path.append(r'D:\Projects and codes\interview\resources')

from slicer import sliceAudio
from transcriber import convertText
from getAnswers import getAnswers
import time
from scoreGenrator import getScore
def banner(text):
    # for loging
    print(f"!! {text} !!\n")
    

banner("converting audio to txt")
givenAnsDB = []
for i in range(0,len(list_paths)):
    
    text = convertText(list_paths[i])
    
    givenAnsDB.append(text)
    
# print(givenAnsDB)

banner("Done") if len(givenAnsDB) == len(list_paths) else banner("Fatal error : Can't convert given part of audio")

# for j in range(len(givenAnsDB)):
    
#     print(f"Result {j} :",givenAnsDB[j])
    
while True:
    
    try:
        banner("Getting answers")
        answerDB = []
        # questionsDB = ["what is machine learning","what is artificial intelligence","what is data science","what is data structure","what is deep learning"]
        questionsDB = ["what is machine learning","what is data science","what is data structure"]

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

for k in range(0,(len(answerDB))):
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
file = open(r'D:\Projects and codes\interview\resources\extinsion_interview\result.txt', 'w')

file.write(f'{totalScore}')

file.close()

banner("completed execution")