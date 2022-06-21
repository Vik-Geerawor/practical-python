"""
Loads the logging config from a json file
and configures the root logger
which is then used everywhere in the code
The root loggers logs to the application.log file
"""


import json
import logging
from logging.config import dictConfig

with open('../config/logger.json') as f:
    logging_config = json.load(f)

dictConfig(logging_config)
