# Student Information Management using YAML and Python

## Overview
This project demonstrates how to read, display, and filter student information stored in a YAML file using Python. The script reads data from `students.yaml`, displays all students, and allows filtering based on GPA.

## Prerequisites
Ensure you have Python installed on your system (Python 3.6+ recommended). You will also need the PyYAML package.

## Installation
To install the required dependencies, run:
```sh
pip install pyyaml
```

## File Structure
```
project-directory/
│── students.yaml
│── app.py
│── README.md
```

## Step 1: Create a YAML File
Create a file named `students.yaml` with the following content:
```yaml
students:
  - name: Alice
    age: 21
    major: Computer Science
    gpa: 3.8
  - name: Bob
    age: 22
    major: Mathematics
    gpa: 3.5
  - name: Charlie
    age: 20
    major: Physics
    gpa: 3.9
  - name: David
    age: 23
    major: Chemistry
    gpa: 3.2
  - name: Eva
    age: 21
    major: Computer Science
    gpa: 3.7
```

## Step 2: Write the Python Script
Create a Python script named `app.py` and add the following code:
```python
import yaml

def load_data(file_path):
    """
    Load data from a YAML file.
    :param file_path: Path to the YAML file.
    :return: Data loaded from the YAML file.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)  # Load the data as a Python dictionary
    return data

def display_students(students):
    """
    Display information about all students.
    :param students: List of student dictionaries.
    """
    print("\nAll Students:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")

def filter_students_by_gpa(students, min_gpa):
    """
    Filter and display students with a GPA above the specified minimum.
    :param students: List of student dictionaries.
    :param min_gpa: Minimum GPA for filtering.
    """
    filtered_students = [s for s in students if s['gpa'] >= min_gpa]
    print(f"\nStudents with GPA >= {min_gpa}:")
    if filtered_students:
        for student in filtered_students:
            print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")
    else:
        print("No students found.")

def main():
    # Load the data from the YAML file
    data = load_data('students.yaml')
    students = data['students']
    
    # Display all students
    display_students(students)
    
    # Filter students by GPA
    min_gpa = float(input("\nEnter minimum GPA to filter students: "))
    filter_students_by_gpa(students, min_gpa)

if __name__ == "__main__":
    main()
```

## Step 3: Run the Application
1. Make sure both `app.py` and `students.yaml` are in the same directory.
2. Open a terminal and navigate to the project directory.
3. Run the script using:
```sh
python app.py
```

## Expected Output
```
All Students:
Name: Alice, Age: 21, Major: Computer Science, GPA: 3.8
Name: Bob, Age: 22, Major: Mathematics, GPA: 3.5
Name: Charlie, Age: 20, Major: Physics, GPA: 3.9
Name: David, Age: 23, Major: Chemistry, GPA: 3.2
Name: Eva, Age: 21, Major: Computer Science, GPA: 3.7

Enter minimum GPA to filter students: 3.6
Students with GPA >= 3.6:
Name: Alice, Age: 21, Major: Computer Science, GPA: 3.8
Name: Charlie, Age: 20, Major: Physics, GPA: 3.9
Name: Eva, Age: 21, Major: Computer Science, GPA: 3.7
```
![img](https://github.com/divyanshsaxena002/YAML-experiment-/blob/main/images/1.png)

![img](https://github.com/divyanshsaxena002/YAML-experiment-/blob/main/images/2.png)



## Conclusion
This project demonstrates how to work with YAML files in Python. You can extend it by adding features such as updating student information, sorting students by GPA, or saving modifications back to the YAML file.

-Divyansh Saxena
