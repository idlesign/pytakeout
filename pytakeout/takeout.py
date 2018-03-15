import os
import inspect

from tempfile import NamedTemporaryFile


def extract_code(func, new_name=None, line_joiner='\n'):
    """Extracts code lines for a given function/method and returns as a string.

    :param func: Function or method to extract code.
    :param str|unicode new_name: New name for a function.
    :param str|unicode line_joiner: String to join code lines with.
    :rtype: str|unicode
    """
    lines = extract_code_lines(func)

    first_line = lines[0]
    indent_len = len(first_line) - len(first_line.lstrip(' '))

    if indent_len:
        indent = ' ' * indent_len
        lines = [line.replace(indent, '', 1) for line in lines]

    name = func.__name__

    if new_name:
        lines[0] = first_line.replace(name, new_name, 1)

    return line_joiner.join(lines)


def extract_code_lines(func, keep_newlines=False):
    """Extracts code lines for a given function/method and returns a list.

    :param func: Function or method to extract code.

    :param bool keep_newlines: Whether to keep newline symbols at the end of each line.

    :rtype: list
    """

    lines = inspect.getsourcelines(func)[0]

    if not keep_newlines:
        lines = [line.rstrip('\n') for line in lines]

    return lines


def code_to_file(code, filepath=None):
    """Saves a given code into a given or temporary file and returns its filepath.

    :param str|unicode code:
    :param str|unicode filepath: If not set temporary file will be generated.
    :rtype: str|unicode
    """
    if filepath is None:
        with NamedTemporaryFile(suffix='.py', delete=False) as f:
            filepath = f.name

    else:
        filepath = os.path.abspath(filepath)

    with open(filepath, 'w') as target_file:
        target_file.write(code)
        target_file.flush()

    return filepath
