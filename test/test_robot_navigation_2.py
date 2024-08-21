import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation


# Test 2: Check for unhandled pylint warnings
def test_pylint_warnings():
    result = subprocess.run(['pylint', 'student_code.py'], capture_output=True, text=True)
    assert "W0" not in result.stdout, "Pylint warnings found"
