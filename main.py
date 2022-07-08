from platform import python_version


correct_python_version = "3.10.5"

if python_version() != correct_python_version:
    print("This program requires Python version 3.10.5")
    exit(1)
