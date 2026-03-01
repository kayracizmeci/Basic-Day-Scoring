
import json # For saving
import os


os.chdir(os.path.dirname(os.path.abspath(__file__))) # For not crashing while not running on IDE


def save(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def load():
    try:
        with open('data.json', 'r') as file:
            content = file.read()
            if not content:
                raise ValueError('File is empty!') # For not crashing if save file is modified by the user.
            return json.loads(content)
    except (FileNotFoundError, ValueError, json.JSONDecodeError):
        log = {'good': 0, 'bad': 0}
        save(log)
        return log


def save_decorator(func):
    def wrapper(poi, g, b):
        log, updated_g, updated_b = func(poi, g, b) # Runs the given func for, us it's calculate_global_score function.
        save(log)
        return log, updated_g, updated_b
    return wrapper


@save_decorator
def calculate_global_score(poi, g, b):
    if poi >= 0: # Filters the input. If the value is negative then it is considered bad bars value. But we don't really use the input negative it's only for filtering.
        g = g + poi
        if b >= 5:
            b = b - 5
    elif poi < 0:
       poi = abs(poi)
       b = b + poi
       if g >= 5:
           g = g - 5
    log = {'good': g, 'bad': b} # Creates a dictionary for saving.
    return log, g, b


while True:
    rn_data =  load() # Loads the old data or creates the data.

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
                point_ng = point * 2 # For doing bad bar negative.
                point = point - point_ng
                point = point / 4 # We do this for bad bar to increase slowly.
        except ValueError:
            print('Please answer with an number!')
            continue

        else:
            break

    g_val = rn_data['good']
    bad_val = rn_data['bad']
    calculate_global_score(point, g_val, bad_val) # Start
    rn_data = load()
    g_val = rn_data['good']
    bad_val = rn_data['bad']
    print(f'Your total scores: good bar: {g_val},  bad bar: {bad_val}')
    print(f'Your total global score is {g_val - bad_val}')

    while True:
        q_answer = input('Do you wanna quit? Answer with y or n ').lower()

        if q_answer == 'y':
            print('Closing...')
            exit()
        elif q_answer == 'n':
            break
        else:
            print('Please answer with y or n!')






















