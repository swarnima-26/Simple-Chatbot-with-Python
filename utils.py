import random
import datetime

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return str(datetime.date.today())

def random_response(response_list):
    return random.choice(response_list)