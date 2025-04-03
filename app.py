import yaml
import os

def load_data(file_path):
    """
    Load data from a YAML file safely.
    :param file_path: Path to the YAML file.
    :return: Data loaded from the YAML file.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None  # Return None if file does not exist

    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)  # Load YAML safely
            if data is None or 'students' not in data:
                print("Error: Invalid YAML format. Missing 'students' key.")
                return None
            return data
        except yaml.YAMLError as e:
            print(f"Error loading YAML file: {e}")
            return None

def display_students(students):
    """
    Display information about all students.
    :param students: List of student dictionaries.
    """
    print("\nAll Students:")
    if not students:
        print("No students available.")
        return

    for student in students:
        print(f"Name: {student.get('name', 'N/A')}, Age: {student.get('age', 'N/A')}, "
              f"Major: {student.get('major', 'N/A')}, GPA: {student.get('gpa', 'N/A')}")

def filter_students_by_gpa(students, min_gpa):
    """
    Filter and display students with a GPA above the specified minimum.
    :param students: List of student dictionaries.
    :param min_gpa: Minimum GPA for filtering.
    """
    filtered_students = [s for s in students if isinstance(s.get('gpa'), (int, float)) and s['gpa'] >= min_gpa]
    print(f"\nStudents with GPA >= {min_gpa}:")
    
    if filtered_students:
        for student in filtered_students:
            print(f"Name: {student.get('name', 'N/A')}, Age: {student.get('age', 'N/A')}, "
                  f"Major: {student.get('major', 'N/A')}, GPA: {student.get('gpa', 'N/A')}")
    else:
        print("No students found.")

def main():
    # Get absolute path to the YAML file
    yaml_path = os.path.join(os.path.dirname(__file__), 'students.yaml')

    # Load the data
    data = load_data(yaml_path)
    if data is None:
        return  # Exit if there's an issue with the file

    students = data.get('students', [])
    
    # Display all students
    display_students(students)
    
    # Filter students by GPA with input validation
    while True:
        try:
            min_gpa = float(input("\nEnter minimum GPA to filter students: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid GPA (numeric value).")

    filter_students_by_gpa(students, min_gpa)

if __name__ == "__main__":
    main()
