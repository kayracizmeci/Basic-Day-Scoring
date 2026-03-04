

import json  # For saving
import os
import datetime
import time
import sys
import matplotlib
matplotlib.use('TkAgg') # For not crashing
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # For not crashing while not running on IDE


def save(new_log):
    try:
        with open('data.json', 'r') as file:
            save_data = json.load(file)
        if type(save_data) is not list:
            save_data = []
    except (FileNotFoundError, json.JSONDecodeError):
        save_data = []

    save_data.append(new_log)
    with open('data.json', 'w') as file:
        json.dump(save_data, file)


def loader():
    try:
        with open('data.json', 'r') as file:
            save_data = json.load(file)
            if len(save_data) > 0:
                return save_data[-1]
            else:
                return {'gbg': 0, 'bbg': 0}
    except (FileNotFoundError, json.JSONDecodeError):
        return {'gbg': 0, 'bbg': 0}


def save_decorator(func):
    def wrapper(poi, gbg, bbg):
        log, gbg, bbg = func(poi, gbg, bbg)
        save(log)
        return log, gbg, bbg

    return wrapper


@save_decorator  # Filters the input. If the value is negative then it is considered bad bars value. But we don't really use the input negative it's only for filtering.
def calculate_global_score(poi, gbg, bbg):
    r_poi = poi
    if poi >= 0:
        gob = 'good'
        gbg = gbg + poi
        if bbg >= 5:
            bbg = bbg - 5
    elif poi < 0:
        gob = 'bad'
        poi = abs(poi)
        bbg = bbg + poi
        if gbg >= 5:
            gbg = gbg - 5

    rigth_now = datetime.datetime.now()
    time_str = rigth_now.strftime("%Y-%m-%d %H:%M:%S")
    log = {'gbg': gbg, 'bbg': bbg, 'cv': r_poi, 'gob': gob, 'time': time_str}  # Creates a dictionary for saving.
    return log, gbg, bbg


def show_graph():
    with open('data.json', 'r') as file:
        save_data = json.load(file)

    if save_data == []:
        print('There is no data for graph')
        return

    dates = [log['time'] for log in save_data]
    good_bar = [log['gbg'] for log in save_data]
    bad_bar = [log['bbg'] for log in save_data]

    plt.figure(figsize=(10, 5))

    plt.plot(dates, good_bar, label='Good Bar', color='green', marker='o')
    plt.plot(dates, bad_bar, label='Bad Bar', color='red', marker='x')

    plt.title('Good Bar/Bad Bar')
    plt.xlabel('Time')
    plt.ylabel('Points')
    plt.xticks(rotation=60)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


while True:
    rn_data = loader()  # Loads the old data or creates the data.

    print('BASIC DAY SCORING')
    print('What did you done this day?')

    while True:
        g_or_b = str(input('good or bad? (answer with g or b) ')).lower()
        if g_or_b not in ['g', 'b']:
            print('Please answer with g or b!')
            continue
        else:
            break

    while True:
        try:
            point = float(input('How much points? '))
            if g_or_b == 'b':
                point_ng = point * 2  # For doing bad bar negative.
                point = point - point_ng
                point = point / 4  # We do this for bad bar to increase slowly.
        except ValueError:
            print('Please answer with an number!')
            continue

        else:
            break

    g_val = rn_data['gbg']
    bad_val = rn_data['bbg']
    calculate_global_score(point, g_val, bad_val)  # Start
    rn_data = loader()
    g_val = rn_data['gbg']
    bad_val = rn_data['bbg']
    print(f'Your total scores: good bar: {g_val},  bad bar: {bad_val}')
    print(f'Your total global score is {g_val - bad_val}')
    print('Showing graph..')
    time.sleep(2)
    show_graph()

    while True:
        q_answer = input('Do you wanna quit? Answer with y or n ').lower()

        if q_answer == 'y':
            print('Closing...')
            sys.exit()
        elif q_answer == 'n':
            break
        else:
            print('Please answer with y or n!')

