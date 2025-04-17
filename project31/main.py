# main.py

import time
from data_collection import collect_data
from performance_analyzer import analyze_performance
from ai_model import predict_performance
from visualization import visualize_results
from optimization_suggestions import suggest_optimizations

def main():
    print("🚀 Starting AI-powered Performance Analyzer for OS Processes...\n")
    
    step = 0  # This keeps track of the time steps for the graph

    while True:
        step += 1

        # 🟡 Step 1: Collect system performance data
        data = collect_data()
        print(f"[{step}] 🔍 System Data: {data}")

        # 🔵 Step 2: Analyze performance to detect bottlenecks
        bottlenecks = analyze_performance(data)
        if bottlenecks:
            print("⚠️  Detected Bottlenecks:")
            for b in bottlenecks:
                print(f"   - {b}")

        # 🟢 Step 3: Suggest optimizations based on detected bottlenecks
        suggestions = suggest_optimizations(bottlenecks)
        if suggestions:
            print("💡 Optimization Suggestions:")
            for s in suggestions:
                print(f"   - {s}")

        # 🔮 Step 4: Predict future CPU usage using a simple AI model
        prediction = predict_performance(data)
        print(f"📈 Predicted CPU Usage: {float(prediction):.2f}%")


        # 📊 Step 5: Visualize real-time performance and predictions
        visualize_results(data, prediction, step)

        # Wait for 5 seconds before next loop iteration
        time.sleep(5)

if __name__ == "__main__":
    main()
