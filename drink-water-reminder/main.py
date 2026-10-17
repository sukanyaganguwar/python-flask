import time
from datetime import datetime

start_time = input("Enter start time (HH:MM:SS): ")
end_time = input("Enter end time (HH:MM:SS): ")

start_time = datetime.strptime(start_time, "%H:%M:%S").time()
end_time = datetime.strptime(end_time, "%H:%M:%S").time()

while True:
    current_time = datetime.now().time()

    if start_time <= current_time < end_time:
        print("Please sip some water...")
        time.sleep(3)

    elif current_time >= end_time:
        print("End time reached. Stopping program.")
        break

    else:
        print("Waiting for start time...")
        time.sleep(1)

print("Program stopped.")