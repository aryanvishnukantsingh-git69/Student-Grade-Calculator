"""
Student Grade Calculator (PS No. 19)
Course: Programming Fundamentals and Logic Building Using Python (RU-100-01-0021)
Institution: Rungta International Skills University (RISU)
Class: B.Tech CSE / 1st Semester / Section K

Problem Statement:
Create a program that takes a student's marks in five subjects, calculates the total,
percentage, grade and pass/fail result, and allows more students to be entered through a loop.
"""

import sys

# Ensure UTF-8 output encoding across Windows terminals
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

NUM_SUBJECTS = 5
PASS_PERCENTAGE = 40.0


def calculate_total(marks):
    """Return the sum of all marks."""
    return sum(marks)


def calculate_percentage(total, num_subjects=NUM_SUBJECTS):
    """Calculate and return percentage out of 100."""
    return (total / (num_subjects * 100)) * 100


def find_grade(percentage):
    """Return letter grade based on percentage cutoff."""
    if percentage >= 85.0:
        return "A"
    elif percentage >= 70.0:
        return "B"
    elif percentage >= 55.0:
        return "C"
    elif percentage >= 40.0:
        return "D"
    else:
        return "F"


def find_result(percentage):
    """Return 'Pass' if percentage >= 40.0, else 'Fail'."""
    if percentage >= PASS_PERCENTAGE:
        return "Pass"
    else:
        return "Fail"


def read_mark(subject_number):
    """Ask repeatedly until user enters a valid number between 0 and 100."""
    while True:
        value = input(f"Marks for subject {subject_number}: ").strip()
        try:
            mark = float(value)
        except ValueError:
            print("Invalid marks. Enter a number between 0 and 100.")
            continue

        if 0.0 <= mark <= 100.0:
            # Show whole numbers as integers (e.g. 80 instead of 80.0)
            return int(mark) if mark.is_integer() else mark

        print("Invalid marks. Enter a number between 0 and 100.")


def process_student():
    """Read student details, calculate total, percentage, grade, and display result."""
    name = input("Name: ").strip()
    marks = [read_mark(i) for i in range(1, NUM_SUBJECTS + 1)]

    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = find_grade(percentage)
    result = find_result(percentage)

    # Output formatted exactly as specified in PS 19 test cases
    output_line = f"{name} │ Total: {total} │ Percentage: {percentage:.2f}% │ Grade: {grade} │ Result: {result}"
    try:
        print(output_line)
    except UnicodeEncodeError:
        print(output_line.replace("│", "|"))

    return {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }


def main():
    """Main program loop to process one or more students."""
    while True:
        process_student()
        again = input("Another student? ").strip().lower()
        if again not in ("y", "yes"):
            break
        print()


if __name__ == "__main__":
    main()
