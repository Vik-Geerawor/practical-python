import logger
import logging
# import sears
# import bounce
# import mortgage
import pcost
import report


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info('*** Main ***')

    # sears.calc()
    # bounce.run()
    # mortgage.run()
    # total_cost = pcost.portfolio_cost('Data/portfolio.csv')
    # logger.info('Portfolio cost: %.2f', total_cost)

    portfolio = report.read_portfolio('Data/portfolio.csv')

    # prices = report.read_prices('Data/prices.csv')

    # report.calculate_pnl()

# https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/03_Formatting.html
