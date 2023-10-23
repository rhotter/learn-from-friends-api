import requests
import json
import time
import random
import matplotlib.pyplot as plt
import numpy as np

url = "https://learning-exp-api.vercel.app/solve"
# url = "http://localhost:3001/solve"

# List to store the number of persons and corresponding time
num_persons_list = []
avg_time_list = []
stderr_list = []

for num_persons in range(10, 101, 10):  # From 10 to 100 persons, in steps of 10
    durations = []
    
    for _ in range(5):  # Average over 5 runs (ideally this should be the outermost loop)
        # Generate preferences for persons, each submitting 4 random preferences
        preferences = []
        for i in range(num_persons):
            others = [str(j) for j in range(num_persons) if j != i]
            selected_others = random.sample(others, min(4, len(others)))
            preferences.append({
                "name": str(i),
                "out": selected_others
            })
        
        # Construct the data payload
        data = {
            "preferences": preferences,
            "n_blocks": 2,
            "weights": [1, 2, 3, 4],
            "low_priority_weight": 10,
            "exclude_presenters": [],
            "first_time_people": [],
        }
        
        headers = {"Content-Type": "application/json"}
        
        # Measure time before API call
        start_time = time.time()
        
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        # Measure time after API call and calculate duration
        end_time = time.time()
        duration = end_time - start_time
        
        durations.append(duration)
    
    avg_time = np.mean(durations)
    stderr = np.std(durations, ddof=1) / np.sqrt(len(durations))
    
    print(f"Number of people: {num_persons}, Average Time: {avg_time:.4f} seconds, Stderr: {stderr:.4f}")
    
    # Store the number of persons, average time, and standard error
    num_persons_list.append(num_persons)
    avg_time_list.append(avg_time)
    stderr_list.append(stderr)

# Create the scaling plot
plt.figure(figsize=(10, 6))
plt.errorbar(num_persons_list, avg_time_list, yerr=stderr_list, fmt='-o', capsize=5)
plt.xlabel('Number of People')
plt.ylabel('Average API resonse time (seconds)')
plt.title('API Response Time Scaling Plot')
plt.grid(True)
plt.savefig('test/speed_test.png')
plt.show()
