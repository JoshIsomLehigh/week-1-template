import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation

# Test 1: Check for unhandled pylint errors
def test_pylint_errors():
    result = subprocess.run(['pylint', 'student_code.py'], capture_output=True, text=True)
    assert "error" not in result.stdout.lower(), "Pylint errors found"
