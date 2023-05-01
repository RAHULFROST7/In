import json

data = {"Result 1": 23, "Result 2": 30, "Result 3": 54}

# Open a file for writing
with open(r"resources\extinsion_interview\result.json", "w") as f:
    # Use json.dump() to write the data to the file
    json.dump(data, f)
