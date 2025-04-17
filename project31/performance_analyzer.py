def analyze_performance(data):
    """
    Analyzes the collected performance data and identifies any bottlenecks.
    """
    cpu_usage = data['cpu_usage']
    memory_usage = data['memory_usage']
    disk_usage = data['disk_usage']
    
    bottlenecks = []
    
    if cpu_usage > 80:  # Example threshold for bottleneck
        bottlenecks.append("CPU usage is high!")
    if memory_usage > 85:  # Example threshold for memory bottleneck
        bottlenecks.append("Memory usage is high!")
    if disk_usage > 90:  # Example threshold for disk bottleneck
        bottlenecks.append("Disk usage is high!")
    
    return bottlenecks
