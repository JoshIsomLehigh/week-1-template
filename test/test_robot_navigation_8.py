import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation




# Test 8: Check proper output format
def test_proper_output_format():
    edges = ["a","b","c","h","z"]
    result = robot_navigation(edges)
    assert isinstance(result, tuple) and len(result) == 2 and isinstance(result[0], int) and isinstance(result[1], str), "Output format is incorrect"

