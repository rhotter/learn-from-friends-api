import requests
import json

url = "http://localhost:3001/solve"

# This is a sample data, replace with actual input
data = {
    "data": [
        {"name": "Person1", "out": ["Person2", "Person3", "Person4", "Person5"]},
        {"name": "Person2", "out": ["Person1", "Person3", "Person4", "Person5"]},
        {"name": "Person3", "out": ["Person1", "Person2", "Person4", "Person5"]},
        {"name": "Person4", "out": ["Person1", "Person2", "Person3", "Person5"]},
        {"name": "Person5", "out": ["Person1", "Person2", "Person3", "Person4"]},
        {"name": "Person6", "out": ["Person1", "Person2", "Person3", "Person4"]},
    ],
    "n_blocks": 2,
    "weights": [1, 2, 3, 4],
    "low_priority_weight": 10,
    "exclude_presenters": [],
    "first_time_people": [],
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print("Status code: ", response.status_code)
print("Response: ", response.json())
