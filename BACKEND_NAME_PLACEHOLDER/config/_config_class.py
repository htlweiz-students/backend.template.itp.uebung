import json
import os

"""
A class for managing database configuration. Provides a singleton pattern and a method to 
load the configuration from a file.

Attributes:
    DB_CONNECTION_STRING (str): Default SQLite in-memory database connection string.
    __instances (dict[str, Config]): A dictionary storing instances of this class keyed by 
                                     their associated file names.

Methods:
    __init__(self, file_name: str = ""): Initializes a new instance with an optional file 
                                         name for loading the configuration.
    _load(self, filename: str) -> None: Loads the database connection string from a JSON file.
    connection_string(self) -> str: Returns the current database connection string.
    get_instance(cls, file_name: str = "") -> Config: Retrieves an instance of this class 
                                              associated with the given file name, creating a 
                                              new one if it doesn't exist yet.
"""


class Config:

    DB_CONNECTION_STRING: str = "sqlite:///:memory:"
    __instances: dict[str, Config] = {}

    def __init__(self, file_name: str = ""):
        if file_name in Config.__instances:
            raise RuntimeError("Don't Call constructor!")
        Config.__instances[file_name] = self
        if file_name:
            self._load(file_name)
        else:
            self._connection_string: str = Config.DB_CONNECTION_STRING

    def _load(self, filename: str) -> None:
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                self._connection_string = json.load(fp=f)["connection_string"]

    """
    Get the current connection string.

    Returns:
        str: The connection string for the database.
    """

    @property
    def connection_string(self) -> str:
        return self._connection_string

    @classmethod
    def get_instance(cls, file_name: str = "") -> Config:
        """
        Returns an instance of the Config class with the given file name. If no file name is provided,
        it will use the default connection string. If an instance already exists for the provided file
        name, it will return that instance instead of creating a new one.

        :param file_name: The file name of the configuration file (optional)
        :return: An instance of the Config class
        """
        if file_name in cls.__instances:
            return cls.__instances[file_name]
        return Config(file_name)
