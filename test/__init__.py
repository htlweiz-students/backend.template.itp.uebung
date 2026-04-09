from . import _00_generate_import

assert _00_generate_import.status
from . import _01_generated_import

test_module = _01_generated_import.test_module


__all__ = ["test_module"]
