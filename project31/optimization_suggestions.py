def suggest_optimizations(bottlenecks):
    """
    Suggests optimizations based on detected bottlenecks.
    """
    suggestions = []
    
    if "CPU usage is high!" in bottlenecks:
        suggestions.append("Consider reducing background processes or optimizing CPU scheduling.")
    if "Memory usage is high!" in bottlenecks:
        suggestions.append("Try closing unused applications or increasing physical memory.")
    if "Disk usage is high!" in bottlenecks:
        suggestions.append("Consider upgrading disk or reducing storage-heavy operations.")
    
    return suggestions
