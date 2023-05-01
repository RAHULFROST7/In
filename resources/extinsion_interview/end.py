import json

data = {"Results": [{"Question":"What is Ml" , "Result": -1},{"What is Data science": -1},{"What is Data Structures": -1}]}

with open(r"resources\extinsion_interview\result.json", "w") as f:
    # Use json.dump() to write the data to the file
    json.dump(data, f)
    
# Create stop recording file
with open('stop_recording', 'w') as f:
    f.write('')
    # 