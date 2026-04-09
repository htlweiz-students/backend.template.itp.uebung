import os

<<<<<<< HEAD
from backend.config import Config
=======
from .. import test_module

Config = test_module.config.Config
>>>>>>> 1f2313428b552dff69506b19f1338c50af95d58e


def test_config_load_file_01():
    test_directory = os.path.dirname(__file__)
    test_config_file_name = os.path.join(test_directory, "test_config.json")
    config = Config.get_instance(test_config_file_name)
    assert "testconnectionstring" == config.connection_string
