import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
    level=logging.DEBUG,
)


"""
Function to get a logger instance with configurable name and log level (debug or info).

Args:
    name (str, optional): Name of the logger. Defaults to __name__ (the name of the current module).
    debug (bool, optional): If True, sets the log level to DEBUG. If False or not provided, sets
    the log level to INFO.

Returns:
    logging.Logger: The instantiated logger object.
"""


def get_logger(name: str = __name__, debug: bool = False):
    logger = logging.getLogger(name)

    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    return logger
