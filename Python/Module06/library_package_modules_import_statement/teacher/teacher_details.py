import os, sys
from os.path import dirname, abspath, join
parent_path = abspath(join(dirname(__file__), '..'))
sys.path.insert(0, parent_path)
from student import student_details
student_details.student()


def teacher():
    print("This is teacher details")