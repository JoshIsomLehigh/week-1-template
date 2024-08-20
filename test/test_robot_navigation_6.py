import subprocess
import re

# Assuming the student's function is named `robot_navigation` and is in a file named `student_code.py`
from student_code import robot_navigation



# Test 6: Check correct output if the target node is not reached
def test_target_not_reached():
    edges = ["a","b","c","e"]
    assert robot_navigation(edges) == (0, "e")
