from ._config_class import Config
from ._logging import get_logger

"""
This module provides two main functions:
1. `Config` - A class for managing application configurations.
2. `get_logger` - A function for getting a logger instance for logging purposes.

These functions are useful in structuring and standardizing the configuration and logging aspects
of an application.
"""
__all__ = [
    "Config",
    "get_logger",
]
