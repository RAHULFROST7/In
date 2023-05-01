import json

data = {
    "results": [
        {
            "question": "What is Ml",
            "result": "-1"
        },
        {
            "question": "What is AI",
            "result":"-1"
        },
        {
            "question": "What is Data Science",
            "result": "-1"
        },
        {
            "question": "What is Data Structures",
            "result": "-1"
        },
        {
            "question": "What is Deepleaning",
            "result": "-1"
        }
    ]
}
with open(r"D:\Projects and codes\interview\resources\extinsion_interview\result.json", "w") as f:
    # Use json.dump() to write the data to the file
    json.dump(data, f)
    
# Create stop recording file
with open('stop_recording', 'w') as f:
    f.write('')
    # 