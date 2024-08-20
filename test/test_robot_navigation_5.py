import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation

# Test 5: Check correct output on invalid input
def test_invalid_input():
    edges = ["a","t","f"]
    assert robot_navigation(edges) == -1
