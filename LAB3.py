import random
import time
import matplotlib.pyplot as plt

# --- Configuration ---
LOG_COUNT = 10  # Number of data points to log
SLEEP_INTERVAL = 0.5  # Seconds to wait between readings
CSV_FILENAME = "sensor_log.csv"
TXT_FILENAME = "sensor_log.txt"

# --- Data Storage ---
timestamps = []
temperatures = []
humidities = []

print("Starting data logging...")

# --- Main Logging Loop ---
for i in range(LOG_COUNT):
    try:
        # 1. Simulate sensor readings
        # Temperature: around 25°C
        temp = 25 + random.uniform(-2.5, 2.5)
        # Humidity: around 60%
        humidity = 60 + random.uniform(-5, 5)

        # Append data to lists for plotting
        timestamps.append(i)
        temperatures.append(temp)
        humidities.append(humidity)

        # Create a formatted string for the log entry
        log_entry = f"Time: {i}s, Temp: {temp:.2f}C, Humidity: {humidity:.2f}%"
        print(log_entry)

        # 2. Log to CSV file
        try:
            with open(CSV_FILENAME, "a") as csv_file:
                # Add header if the file is new/empty
                if i == 0:
                    csv_file.write("Timestamp (s),Temperature (C),Humidity (%)\n")
                csv_file.write(f"{i},{temp:.2f},{humidity:.2f}\n")
        except IOError as e:
            print(f"Error: Could not write to {CSV_FILENAME}. Details: {e}")

        # 3. Log to TXT file
        try:
            with open(TXT_FILENAME, "a") as txt_file:
                txt_file.write(log_entry + "\n")
        except IOError as e:
            print(f"Error: Could not write to {TXT_FILENAME}. Details: {e}")

        # Wait before the next reading
        time.sleep(SLEEP_INTERVAL)

    except Exception as e:
        print(f"An unexpected error occurred during the main loop: {e}")

print("\nData logging complete.")

# --- Data Visualization ---
try:
    print("Generating plots...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.suptitle('Sensor Data Logs', fontsize=16)

    # Plot Temperature
    ax1.plot(timestamps, temperatures, 'r-o', label='Temperature')
    ax1.set_ylabel("Temperature (C)")
    ax1.set_title("Temperature over Time")
    ax1.grid(True)
    ax1.legend()

    # Plot Humidity
    ax2.plot(timestamps, humidities, 'b-s', label='Humidity')
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Humidity (%)")
    ax2.set_title("Humidity over Time")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    print("Plot displayed successfully.")

except Exception as e:
    print(f"An error occurred during plotting: {e}")