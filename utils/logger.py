import logging
import os
from datetime import datetime

# Define the path to the log file
LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "logs",
                        f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for the log file
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)

# Create a console handler for the standard output stream
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter for the log messages
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def log_info(message):
    """
    This function logs an info-level message to the log file and the console.
    """
    logger.info(message)


def log_error(message):
    """
    This function logs an error-level message to the log file and the console.
    """
    logger.error(message)
