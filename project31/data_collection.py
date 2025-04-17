# data_collection.py
import psutil

def collect_data():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    data = {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage
    }
    
    print(f"Collected Data: {data}")  # Print the collected data to see if it changes.
    return data
