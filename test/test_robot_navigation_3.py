import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation



# Test 3: Check for unhandled pylint style recommendations
def test_pylint_style():
    result = subprocess.run(['pylint', 'student_code.py'], capture_output=True, text=True)
    assert "C0" not in result.stdout, "Pylint style recommendations found"
