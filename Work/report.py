# report.py
#
# Exercise 2.4
import sys
import csv
import logging
import pcost

logger = logging.getLogger(__name__)


def read_portfolio(filename):
    """
    Reads data from a file containing portfolio data and
    returns a list of tuples containing each holding
    """
    logger.info('Reading portfolio data from file %s', filename)
    portfolio = []
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)

            for row in rows:
                try:
                    name = row[0]
                    shares = int(row[1])
                    price = float(row[2])

                    # list of tuples
                    # portfolio.append((name, shares, price))

                    # list of dicts
                    portfolio.append(dict(zip(headers, [name, shares, price])))
                    logger.info('%s, %d, %.2f', name, shares, price)
                except ValueError:
                    print(f'Bad data')
                    continue
    except FileNotFoundError:
        print(f'Please check filename')

    return portfolio


def read_prices(filename):
    """
    Reads stock prices from a file and
    returns a dictionary contains prices of shares
    """
    logger.info('Reading price data from file %s', filename)
    prices = {}
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            for row in rows:
                try:
                    prices[row[0]] = float(row[1])
                    logger.info('%s: %s', row[0], row[1])
                except ValueError:
                    logger.error('Bad data in file %s', filename)
                except IndexError:
                    logger.error('Empty line in file %s', filename)
    except FileNotFoundError:
        logger.error('File not found: %s', filename)

    return prices


def calculate_pnl():
    total_cost = pcost.portfolio_cost('Data/portfolio.csv')
    logger.info('Portfolio cost: %.2f', total_cost)

    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')

    pv = 0.0
    for holding in portfolio:
        name = holding['name']
        if name in prices:
            logger.info('%s: price - old %.2f new %.2f', name, holding['price'], prices[name])
            pv += holding['shares'] * prices[name]
    logger.info('PV of portfolio %.2f', pv)
    pnl = pv - total_cost
    print(f'Daily PnL: {pnl:.2f}')
    logger.info('Daily PnL %.2f', pnl)
