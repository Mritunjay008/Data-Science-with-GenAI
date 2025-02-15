# Library, Package, and Module Definitions

## Why Separate Scripts for Students and Teachers?

Keeping separate scripts for **student details** and **teacher details** ensures:

- **Better Code Organization**: Code is easier to manage and understand.
- **Improved Maintainability**: Each component is separate and reusable.
- **Best Practices**: Different functionalities should be modularized.
- **Example**: Model training and Exploratory Data Analysis (EDA) should be kept in separate scripts.

---

## What is a Module?

A **module** is a single file with a `.py` extension that contains Python code. It may include functions, classes, variables, or any other Python code.

### Example:
```
student_details.py  # Module handling student-related functionality
teacher_details.py  # Module handling teacher-related functionality
```

### Illustration:
```
+----------------------+
|  student_details.py  |
|----------------------|
| def add_student():   |
| def remove_student():|
+----------------------+

+----------------------+
|  teacher_details.py  |
|----------------------|
| def add_teacher():   |
| def remove_teacher():|
+----------------------+
```

---

## What is a Package?

A **package** is a collection of related **modules**, organized in directories.
Each package should contain an `__init__.py` file (though optional in modern Python) to be recognized as a package.

### Example:
```
student/                 # Package
|-- __init__.py          # Marks it as a package
|-- student_details.py   # Module
|-- student_grades.py    # Another module
```

### Illustration:
```
+----------------+
| student/       |
|----------------|
| __init__.py    |
| student_details.py |
| student_grades.py  |
+----------------+

+----------------+
| teacher/       |
|----------------|
| __init__.py    |
| teacher_details.py |
| teacher_schedule.py |
+----------------+
```

---

## Importing Modules and Packages

To use modules inside a package, we use **import**:

```python
from student import student_details
student_details.add_student()
```

To import specific functions:
```python
from teacher.teacher_details import add_teacher
add_teacher()
```

---

This structured approach makes the code **scalable, readable, and maintainable**.

