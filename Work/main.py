import logger
import logging
import sears
import bounce
import mortgage


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info('*** Main ***')

    # sears.calc()
    # bounce.run()
    mortgage.run()


# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/04_Strings.html
