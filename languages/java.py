# languages/java.py
import subprocess
from typing import Dict

def compile_and_run_java(code: str) -> Dict[str, str]:
    with open('Solution.java', 'w') as f:
        f.write(code)
    
    compile_result = subprocess.run(['javac', 'Solution.java'], capture_output=True, text=True)
    
    if compile_result.returncode != 0:
        return {
            'stdout': '',
            'stderr': compile_result.stderr
        }
    
    run_result = subprocess.run(['java', 'Solution'], capture_output=True, text=True)
    return {
        'stdout': run_result.stdout,
        'stderr': run_result.stderr
    }
