#!/usr/bin/env python
import numpy as np

def read_timestamps(input_file):
    """
    Read file with timestamps, and return a sorted list of the lines
    """
    timestamps = []
    with open(input_file) as input:
        for line in input:
            timestamps.append(line)
    timestamps.sort(key = lambda x: x.split("]")[0])
    return timestamps

class Guard:
    def __init__(self, id):
        self.id = id
        self.total_sleep = 0
        self.minutes = np.zeros(60)

    def sleep(self, start, end):
        self.total_sleep += (end - start)
        self.minutes[start:end] += 1
        
    def get_most_slept_minute(self):
        return np.argmax(self.minutes)

if __name__ == "__main__":
    timestamps = read_timestamps("input.txt")
    guards = {}
    current_ID = 0
    sleep_start = None

    # Process data
    for entry in timestamps:
        time = entry.split(" ")[1][:-1]
        event = entry.split("] ")[1]

        if event.startswith("Guard"):
            current_ID = entry.split('#')[1].split(' ')[0]
            if current_ID not in guards:
                guards[current_ID] = Guard(current_ID)

        elif event.startswith("falls asleep"):
            sleep_start = time[3:]

        elif event.startswith("wakes up"):
            guards.get(current_ID).sleep(int(sleep_start), int(time[3:]))
            sleep_start = None

    # Find ID of sleepmaster
    longest_sleeptime = 0
    sleepmaster_ID = -1
    for key in guards.keys():
        if guards[key].total_sleep > longest_sleeptime:
            longest_sleeptime = guards[key].total_sleep
            sleepmaster_ID = guards[key].id

    most_frequent_minute = guards[sleepmaster_ID].get_most_slept_minute()

    print("Guard with ID", sleepmaster_ID, "slept the longest, at",
          longest_sleeptime, "minutes.")
    print("He slept most often on minute", most_frequent_minute)
    print("Multiplying these, we have", int(sleepmaster_ID) * most_frequent_minute,
          "which is our puzzle answer.")
