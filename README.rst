pytakeout
=========
https://github.com/idlesign/pytakeout

|release| |lic| |ci| |coverage| |health|

.. |release| image:: https://img.shields.io/pypi/v/pytakeout.svg
    :target: https://pypi.python.org/pypi/pytakeout

.. |lic| image:: https://img.shields.io/pypi/l/pytakeout.svg
    :target: https://pypi.python.org/pypi/pytakeout

.. |ci| image:: https://img.shields.io/travis/idlesign/pytakeout/master.svg
    :target: https://travis-ci.org/idlesign/pytakeout

.. |coverage| image:: https://img.shields.io/coveralls/idlesign/pytakeout/master.svg
    :target: https://coveralls.io/r/idlesign/pytakeout

.. |health| image:: https://landscape.io/github/idlesign/pytakeout/master/landscape.svg?style=flat
    :target: https://landscape.io/github/idlesign/pytakeout/master


Description
-----------

*Simplifies Python code extraction*

With this you can easily:

* extract function/method/class source code;
* perform basic code transformations;
* save code into a file.


Sample
------

.. code-block:: python

    from pytakeout import extract_code, code_to_file


    def func_to_extract():
        # This function needs to be extracted.
        return True


    # Extract code as a string.
    code = extract_code(func_to_extract)

    # Save it into a temporary file.
    tmp_code_file = code_to_file(code)
