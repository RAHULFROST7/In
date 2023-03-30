from resources.transcriber import convertText
from resources.scoreGenrator import getScore
from resources.slicer import sliceAudio
from resources.getAnswers import getAnswers
def banner(text):
    # for loging
    print(f"!! {text} !!\n")
    
    
def feroz():
    
    return r"D:\Projects and codes\interview\resources\test_audio_e_airport.mp3"


def main():
    
    # recording audio
    banner("getting audio path from feroz")
    path = feroz()
    
    banner("Done") if len(path) != 0 else banner("Fatal Error : Failed fetching path")
    
    # slicing
    banner("Spliting audio")
    list_paths = sliceAudio(path=path)
    banner('Done')
    # print(list_paths)
    
    banner("converting audio to txt")
    givenAnsDB = []
    for i in range(0,len(list_paths)):
        
        text = convertText(list_paths[i])
        givenAnsDB.append(text)
    # print(audio_text)
    
    banner("Done") if len(givenAnsDB) == len(list_paths) else banner("Fatal error : Can't convert given part of audio")
    # for j in range(len(audio_text)):
        # 
        # print(f"Result {j} :",audio_text[j])
    
    banner("Getting answers")
    answerDB = []
    questionsDB = ["what is machine learning","what is artificial intelligence","what is data science","what is data structure","what is deep learning"]
    for i in range(0,len(questionsDB)):
        
       temp_list = getAnswers(questionsDB[i])
       answerDB.append(temp_list)
    # print(answerDB) 
    banner("Done") if len(answerDB) == len(questionsDB) == len(givenAnsDB) else banner("Fatal Error : Can't fetch answers")
    
    banner("Comparing for score")
    
    ansScores = []
    for k in range(0,len(answerDB)):
        temp = getScore(answerDB[k],givenAnsDB[k])
        ansScores.append(temp)
        
    total = 0
    for l in range(0,len(ansScores)):
        total += ansScores[l]
        
    totalScore = total/len(ansScores)
    print(totalScore)
    banner("Done")
    

if __name__ == "__main__":
    main()
    

# pytutify