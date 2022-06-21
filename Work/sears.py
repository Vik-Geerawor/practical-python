import logging

logger = logging.getLogger(__name__)


def calc():
    BILL_THINKNESS = 0.11 * 0.001  # Meters (0.11 mm)
    SEARS_HEIGHT = 442  # Height (meters)
    num_bills = 1
    day = 1

    while num_bills * BILL_THINKNESS < SEARS_HEIGHT:
        print(day, num_bills, num_bills * BILL_THINKNESS)
        day = day + 1
        num_bills = num_bills * 2

    print('Number of days', day)
    print('Number of bills', num_bills)
    print('Final height', num_bills * BILL_THINKNESS)
    logger.info('%d days and %d bills to reach %dm height', day, num_bills, num_bills * BILL_THINKNESS)
