import datetime

def starttime():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return now

# Call the function and store the time in a variable
start_time = starttime()

print("The start time is", start_time)
