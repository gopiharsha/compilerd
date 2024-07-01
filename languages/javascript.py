# languages/javascript.py
import subprocess
from typing import Dict

def compile_and_run_javascript(code: str) -> Dict[str, str]:
    with open('solution.js', 'w') as f:
        f.write(code)
    
    result = subprocess.run(['node', 'solution.js'], capture_output=True, text=True)
    return {
        'stdout': result.stdout,
        'stderr': result.stderr
    }
