# ai_model.py

import numpy as np
from sklearn.linear_model import LinearRegression
from collections import deque

# History buffer (for training)
cpu_history = deque(maxlen=10)
time_steps = deque(maxlen=10)

# Start with 1 step (to avoid empty training)
counter = 0

def predict_performance(data):
    global counter
    counter += 1

    cpu_usage = data['cpu_usage']
    cpu_history.append(cpu_usage)
    time_steps.append(counter)

    # Not enough data to train? Just return current usage
    if len(cpu_history) < 3:
        return float(cpu_usage)

    # Train simple linear regression model
    X = np.array(time_steps).reshape(-1, 1)
    y = np.array(cpu_history)
    model = LinearRegression()
    model.fit(X, y)

    next_step = np.array([[counter + 1]])
    prediction = model.predict(next_step)[0]  # Get scalar from array
    return float(prediction)
