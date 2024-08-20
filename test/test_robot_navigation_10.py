import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation


# Test 10: Check proper cycle handling
def test_cycle_handling():
    edges = ["a","d","f","e","d"]
    assert robot_navigation(edges) == -2