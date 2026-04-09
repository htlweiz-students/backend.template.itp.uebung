from sqlalchemy import Engine, create_engine

from backend.config import Config
from backend.model import Base


def get_engine(config_file: str = "") -> Engine:
    """
    This function initializes a SQLAlchemy engine by reading the configuration from a given file
    and creating all tables if they don't exist.

    :param config_file: A string specifying the location of the configuration file. If not
                        provided, it defaults to an empty string.
    :return: An initialized SQLAlchemy Engine object.
    """
    config = Config.get_instance(config_file)
    engine = create_engine(config.connection_string)
    Base.metadata.create_all(engine)
    return engine
