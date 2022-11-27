"""
Loads the logging config from a json file
and configures the root logger
which is then used everywhere in the code
The root loggers logs to the application.log file
"""

import os
import json
from logging.config import dictConfig

# ensures that the logs dir is present in the root dir
logs_dir = "../logs"

if not (os.path.isdir(logs_dir)):
    os.mkdir(logs_dir)


with open('../config/logger.json') as f:
    logging_config = json.load(f)

dictConfig(logging_config)
