# visualization.py

import matplotlib.pyplot as plt

# Enable interactive plotting
plt.ion()

# Store historical data (keeps last 20 points)
cpu_history = []
prediction_history = []
time_ticks = []

def visualize_results(data, prediction, step):
    cpu_usage = data['cpu_usage']
    predicted_cpu = prediction

    # Add new values to history
    cpu_history.append(cpu_usage)
    prediction_history.append(predicted_cpu)
    time_ticks.append(step)

    # Limit to last 20 entries to avoid clutter
    max_length = 20
    if len(cpu_history) > max_length:
        cpu_history.pop(0)
        prediction_history.pop(0)
        time_ticks.pop(0)

    # Clear old plot
    plt.clf()

    # Plot actual CPU usage
    plt.plot(time_ticks, cpu_history, label='CPU Usage', color='blue', marker='o')

    # Plot predicted CPU usage
    plt.plot(time_ticks, prediction_history, label='Predicted CPU Usage', color='red', linestyle='--', marker='x')

    # Customize graph
    plt.title('Real-Time CPU Usage and AI Prediction')
    plt.xlabel('Time Step')
    plt.ylabel('CPU Usage (%)')
    plt.ylim(0, 100)  # Set y-axis from 0 to 100%
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Draw updated plot
    plt.draw()
    plt.pause(0.1)  # Allow brief time for the plot to render
