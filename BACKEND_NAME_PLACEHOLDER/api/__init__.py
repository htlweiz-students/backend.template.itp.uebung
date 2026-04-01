"""
Function for building the application.

This function initializes and returns the Flask app instance.

:return: A Flask app instance
"""

from ._app import build_app

__all__ = ["build_app"]
