# logger.py

import csv
from datetime import datetime

def log_to_csv(data, prediction, top_processes, filename="performance_log.csv"):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            datetime.now(),
            data['cpu_usage'],
            data['memory_usage'],
            data['disk_usage'],
            prediction,
            "; ".join([f"{p['name']}({p['cpu_percent']}%)" for p in top_processes])
        ])
