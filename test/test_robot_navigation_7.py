import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation




# Test 7: Check proper input format
def test_proper_input_format():
    edges = ["a-b-1", "b-c-2", "c-j-3", "j-z-2"]
    assert isinstance(edges, list) and all(isinstance(edge, str) for edge in edges), "Input format is incorrect"

