<<<<<<< HEAD
import backend


def test_config_00() -> None:
    config = backend.config.Config.get_instance()
=======
from .. import test_module

Config = test_module.config.Config


def test_config_00() -> None:
    config = Config.get_instance()
>>>>>>> 1f2313428b552dff69506b19f1338c50af95d58e
    assert config

    assert "sqlite:///:memory:" == config.connection_string
