# bounce.py
#
# Exercise 1.5

import logging


def run():
    logger = logging.getLogger(__name__)
    height = 100
    num_of_bounce = 10
    bounce_factor = 3/5

    logger.info('Dropping the ball')
    for i in range(1, 11):
        height *= bounce_factor
        print(i, round(height, 4))
        logger.info('Bounce %d, height %d', i, round(height))
