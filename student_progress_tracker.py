
# student_progress_tracker.py

def calculate_weighted_average(grades, weights):
    return sum(g * w for g, w in zip(grades, weights)) / sum(weights)

def get_status(average):
    if average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Average"
    else:
        return "Needs Improvement"

def main():
    print("Welcome to the Student Progress Tracker!\n")
    students = {}

    while True:
        name = input("Enter student's name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        num_courses = int(input(f"How many courses has {name} taken? "))
        grades, weights = [], []

        for i in range(num_courses):
            course = input(f"  Course {i+1} name: ")
            grade = float(input(f"  Grade for {course}: "))
            weight = float(input(f"  Weight for {course} (e.g., 1 for standard, 2 for major): "))
            grades.append(grade)
            weights.append(weight)

        avg = calculate_weighted_average(grades, weights)
        students[name] = (avg, get_status(avg))

    print("\n--- Student Progress Report ---")
    for student, (avg, status) in students.items():
        print(f"{student}: {avg:.2f} - {status}")

if __name__ == "__main__":
    main()
