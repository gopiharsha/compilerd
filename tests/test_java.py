# tests/test_java.py
from languages.java import compile_and_run_java

def test_java_hello_world():
    code = '''
public class Solution {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
'''
    result = compile_and_run_java(code)
    assert result['stdout'] == "Hello, World!\n"
    assert result['stderr'] == ""
