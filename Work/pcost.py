# pcost.py
#
# Exercise 1.27
import sys
import csv
import logging

logger = logging.getLogger(__name__)


def portfolio_cost(filename):
    """
    Calculates the total cost of a portfolio
    param: filename containing quantity and price
    """
    logger.info('Calculating portfolio cost')
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            # print(headers)
            cost = 0.0

            for row in rows:
                try:
                    name = row[0]
                    shares = int(row[1])
                    price = float(row[2])
                    logger.info('%s, %d, %f', name, shares, price)
                except ValueError:
                    print(f'Bad data')
                    logger.error('Bad data in file %s', filename)
                    continue

                cost += shares * price

            return cost

    except FileNotFoundError:
        print(f'Please check filename')
        logger.error('File not found: %s', filename)


# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'
#
# cost = portfolio_cost(filename)
# print('Total cost:', cost)
