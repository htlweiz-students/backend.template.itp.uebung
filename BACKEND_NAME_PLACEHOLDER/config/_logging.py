import logging

from ._config_class import Config

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)


def get_logger(name: str = __name__):
    """
    Function to get a logger instance with configurable name and log level (debug or info).

    Args:
        name (str, optional): Name of the logger. Defaults to __name__ (the name of the current
        module).
    Returns:
        logging.Logger: The instantiated logger object.
    """
    logger = logging.getLogger(name)
    config =Config.get_instance()
    if config.log_level:
        logger.setLevel(config.log_level)
    return logger
