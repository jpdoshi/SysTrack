from PIL import ImageGrab
from datetime import datetime
from random import randint

import time
import os


def capture_screen():
    time_now = datetime.now()

    curr_time = time_now.strftime("%H-%M-%S")
    curr_date = time_now.strftime("%d-%m-%Y")

    if not os.path.exists(curr_date):
        os.makedirs(curr_date)

    filename = curr_date + '/' + curr_time + '.png'

    img = ImageGrab.grab()
    img.save(filename, format='PNG')


if __name__ == '__main__':
    min_limit = 2
    max_limit = 5

    while True:
        delay = randint(min_limit, max_limit)

        time.sleep(delay)
        capture_screen()
