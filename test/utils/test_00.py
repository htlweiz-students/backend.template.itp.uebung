import os

import pytest

<<<<<<< HEAD
from backend import utils
=======
from .. import test_module

utils = test_module.utils
>>>>>>> 1f2313428b552dff69506b19f1338c50af95d58e


def test_00(capfd: pytest.CaptureFixture[str]) -> None:
    utils.test()
    out, err = capfd.readouterr()
    assert "This is a test!" + os.linesep == out
    assert "" == err
