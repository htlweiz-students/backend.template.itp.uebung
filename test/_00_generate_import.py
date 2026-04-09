import glob
import os

status = False

script_dir = os.path.dirname(os.path.abspath(__file__))
dir_name = os.path.dirname(script_dir)

main_files = glob.glob(os.path.join(dir_name, "*/main.py"))

assert len(main_files) == 1

if os.path.exists(main_files[0]):
    assert True
else:
    assert False

module_name = os.path.basename(os.path.dirname(main_files[0]))


with open(os.path.join(script_dir, "_01_generated_import.py"), "w") as generated:
    _ = generated.write(f"""import {module_name} as test_module""")
    _ = generated.write(os.linesep)
    _ = generated.write(os.linesep)
    _ = generated.write(f"""__all__ = ["test_module"]""")
    _ = generated.write(os.linesep)

status = True
