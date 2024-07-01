# languages/python.py
import subprocess
from typing import Dict

def compile_and_run_python(code: str) -> Dict[str, str]:
    with open('solution.py', 'w') as f:
        f.write(code)
    
    result = subprocess.run(['python3', 'solution.py'], capture_output=True, text=True)
    return {
        'stdout': result.stdout,
        'stderr': result.stderr
    }
