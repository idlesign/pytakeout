from tempfile import NamedTemporaryFile

import pytest

from pytakeout import extract_code_lines, extract_code, code_to_file


def func_to_extract():
    line1 = '1'
    return line1


class SomeClass(object):

    def method_to_extract(self):
        return 0


def test_extract_func_lines():

    func_lines = extract_code_lines(func_to_extract)

    assert len(func_lines) == 3

    extracted_str = extract_code(func_to_extract, 'otherfunc', line_joiner='|')

    assert extracted_str == """def otherfunc():|    line1 = '1'|    return line1"""

    extracted_str = extract_code(SomeClass.method_to_extract, line_joiner="|")

    assert extracted_str == 'def method_to_extract(self):|    return 0'

    extracted_str = extract_code(SomeClass, new_name='OtherClass', line_joiner="|")

    assert extracted_str == 'class OtherClass(object):||    def method_to_extract(self):|        return 0'


def test_code_to_file():

    code = 'somecode'

    filepath = code_to_file(code)

    assert filepath.endswith('.py')

    fpath = NamedTemporaryFile(delete=False).name

    assert fpath == code_to_file(code, filepath=fpath)

    with open(filepath) as f:
        assert f.read() == code
