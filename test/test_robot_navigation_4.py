import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation



# Test 4: Check correct output if the target node is reached
def test_correct_output_target_reached():
    nodes = ["a","b","c","h","z"]
    assert robot_navigation(nodes) == (10, "z")

