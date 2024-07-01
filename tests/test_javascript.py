# tests/test_javascript.py
from languages.javascript import compile_and_run_javascript

def test_javascript_hello_world():
    code = 'console.log("Hello, World!")'
    result = compile_and_run_javascript(code)
    assert result['stdout'] == "Hello, World!\n"
    assert result['stderr'] == ""
