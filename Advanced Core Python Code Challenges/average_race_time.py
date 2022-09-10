# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
import math
import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    times = []
    for i in range(1, len(races)):
        race = races[i].split()
        if "Jennifer" in race[1] and "Rhines" in race[2]:
            time = race[0].split(":")
            times.append(float(time[0])*60+float(time[1]))
    return times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    avg = sum(racetimes) / len(racetimes)
    m = str(math.floor(avg / 60))
    s = str(round(avg % 60, 1))
    M = str(round(avg % 1, 1))
    res = f"{m}:{s}"
    return res

print(get_average())