#!/usr/bin/env python

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

    def sleep(self, minutes):
        self.total_sleep += minutes

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
            print("Guard with ID", current_ID, "starts his shift.")
            if current_ID not in guards:
                guards[current_ID] = Guard(current_ID)
                print("Added new guard to list.")

        elif event.startswith("falls asleep"):
            sleep_start = time[3:]
            print("Guard with ID", current_ID, "falls asleep.")

        elif event.startswith("wakes up"):
            guards.get(current_ID).sleep(int(time[3:]) - int(sleep_start))
            print("Guard with ID", current_ID, "wakes up.")
            sleep_start = None

    # Find ID of sleepmaster
    longest_sleeptime = 0
    sleepmaster_ID = -1
    for key in guards.keys():
        if guards[key].total_sleep > longest_sleeptime:
            longest_sleeptime = guards[key].total_sleep
            sleepmaster_ID = guards[key].id

        # print("ID:", guards[key].id, "Sleep:", guards[key].total_sleep)

    print("Guard with ID", sleepmaster_ID, "slept the longest, at",
          longest_sleeptime, "minutes.")
