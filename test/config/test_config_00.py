from .. import test_module

Config = test_module.config.Config


def test_config_00() -> None:
    config = Config.get_instance()
    assert config

    assert "sqlite:///:memory:" == config.connection_string
