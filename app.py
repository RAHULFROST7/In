from resources.transcriber import convertText
from resources.scoreGenrator import getScore

def banner(text):
    # for loging
    print(f"!! {text} !!\n")
    
    
def feroz():
    
    return r"D:\Projects and codes\interview\resources\test_audio_e_airport.mp3"


def main():
    
    banner("getting audio path from feroz")
    path = feroz()
    
    if len(path) != 0:
        banner("Got the path")
    else:
        banner("failed fetching path")
    
    # banner("Spliting audio")
    # splitAudio()
    # banner('Done')
    
    banner("converting audio to txt")
    audio_text = convertText(path)
    banner("Succesfully converted")
    
    
    
    banner("Comparing for score")
    score = getScore(audio_text,"Rahul kldfgjdfmkejew rewpiopwejwzncdKJnasds lsjfsklfja ejkfekjfn ijoefioajaif kf kjjf sfajspfhaif sfih nndioagj s fdf9refj frefjio]")
    print(f"Final Score is : {score}%\n")
    banner("Ran without errors")
    # print(audio_text)
    

if __name__ == "__main__":
    main()
    

    