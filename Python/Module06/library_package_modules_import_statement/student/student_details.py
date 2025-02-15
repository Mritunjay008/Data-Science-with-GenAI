import os
import sys
from os.path import dirname, join, abspath

# Get the absolute path of the parent directory to ensure module imports work correctly
parent_dir_path = abspath(join(dirname(__file__), ".."))
# Insert the parent directory path at the beginning of the system path
sys.path.insert(0, parent_dir_path)

# Import the teacher_details module from the teacher package
# from teacher import teacher_details

# Function to display student details
def student():
    """Displays student details."""
    print("This is student details")

# Call the teacher function from teacher_details module to display teacher details
# teacher_details.teacher()