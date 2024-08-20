import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation

# Test 11: Ensure student_code does not contain specific test case inputs explicitly
def test_no_explicit_test_cases():
    with open('student_code.py', 'r') as file:
        content = file.read()
    forbidden_inputs = [
        '["a","b","c","j","z"]',
        '["a","t","f"]',
        '["a","b","c","e"]',
        '["a","d","f","e","d"]'
    ]
    forbidden_inputs2 = [
        "['a','b','c','j','z']",
        "['a','t','f'",
        "['a','b','c','e']",
        "['a','d','f','e','d']"
    ]
    for forbidden_input in forbidden_inputs:
        assert forbidden_input not in content, f"Explicit test case input {forbidden_input} found in student_code.py"
    for forbidden_input in forbidden_inputs2:
        assert forbidden_input not in content, f"Explicit test case input {forbidden_input} found in student_code.py"
