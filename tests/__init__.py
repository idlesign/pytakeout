import sys
from pathlib import Path
import unittest


DIR_CURRENT = Path(__file__).resolve().parent
DIR_PARENT = DIR_CURRENT.parent

sys.path.insert(0, DIR_PARENT)

tests_loader = unittest.TestLoader()
test_suit = tests_loader.discover(DIR_CURRENT)
unittest.TextTestRunner().run(test_suit)

