import logger
import logging
# import sears
# import bounce
# import mortgage
import pcost
# import report


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info('*** Main ***')

    # sears.calc()
    # bounce.run()
    # mortgage.run()
    total_cost = pcost.portfolio_cost('Data/portfolio.csv')
    print(f'Total cost of portfolio is {total_cost}')

    # report.read_portfolio('Data/portfolio.csv')


# https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/02_Containers.html
