# tests/test_python.py
from languages.python import compile_and_run_python

def test_python_hello_world():
    code = 'print("Hello, World!")'
    result = compile_and_run_python(code)
    assert result['stdout'] == "Hello, World!\n"
    assert result['stderr'] == ""
