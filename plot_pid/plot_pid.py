import pandas as pd
import matplotlib.pyplot as plt

# Load the log file
log_file = "pid_log.txt"

try:
    # Read CSV into DataFrame
    df = pd.read_csv(log_file)

    # Plot PID error over time
    plt.figure(figsize=(10, 6))

    # Error plot
    plt.subplot(3, 1, 1)
    plt.plot(df["Time"], df["Error"], label="Error", color="red")
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.ylabel("Error")
    plt.legend()

    # P, I, D values over time
    plt.subplot(3, 1, 2)
    plt.plot(df["Time"], df["P"], label="P-Gain", color="blue")
    plt.plot(df["Time"], df["I"], label="I-Gain", color="green")
    plt.plot(df["Time"], df["D"], label="D-Gain", color="orange")
    plt.ylabel("PID Values")
    plt.legend()

    # Correction plot
    plt.subplot(3, 1, 3)
    plt.plot(df["Time"], df["Correction"], label="Correction", color="purple")
    plt.ylabel("Correction")
    plt.xlabel("Time (ms)")
    plt.legend()

    plt.suptitle("PID Line Following Analysis")
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(
        f"Error: The file {log_file} was not found. Ensure you have copied it from the SPIKE Prime hub.")
except Exception as e:
    print(f"An error occurred: {e}")
