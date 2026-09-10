def get_letter_grade(percentage):
    """Maps a numerical percentage to a letter grade using a loop and dictionary."""
    grade_scale = {
        "A": 90,
        "B": 80,
        "C": 70,
        "D": 60,
        "F": 0,
    }
    for grade, minimum_score in grade_scale.items():
        if percentage >= minimum_score:
            return grade
    return "F"


def collect_assignments():
    """Uses a while loop to store assignments and their data in a dictionary."""
    gradebook = {}
    print("--- Enter Course Assessments ---")
    print("Type 'done' when you are finished entering assignments.\n")

    while True:
        name = input("Assignment name (or 'done'): ").strip()
        if name.lower() == "done":
            """If there is no assignments added"""
            if not gradebook:
                print("Please enter at least one assignment before finishing.\n")
                continue
            break

        try:
            score = float(input(f"Score for '{name}' (0-100): "))
            weight = float(input(f"Weight for '{name}' (e.g., 20 for 20%): "))
            
            # Store in nested dictionary format:
            # { "Midterm": {"score": 85.0, "weight": 25.0} }
            gradebook[name] = {"score": score, "weight": weight}
            print(f"Added {name}.\n")
        except ValueError:
            print("Invalid input. Please enter numeric values for score and weight.\n")

    return gradebook


def calculate_final_grade(gradebook):
    """Loops through the dictionary to compute the weighted average."""
    total_weighted_points = 0.0
    total_weight = 0.0

    # Loop through dictionary items
    for details in gradebook.values():
        score = details["score"]
        weight = details["weight"]

        total_weighted_points += score * (weight / 100)
        total_weight += weight

    if total_weight == 0:
        return 0.0, "N/A"

    # Normalize to 100% in case entered weights don't sum to exactly 100
    normalized_score = (total_weighted_points / total_weight) * 100
    letter = get_letter_grade(normalized_score)

    return normalized_score, letter


def display_report(gradebook, final_score, letter_grade):
    """Prints a structured summary table of the grades."""
    print("\n" + "=" * 45)
    print(f"{'Assignment':<20}{'Score':<12}{'Weight':<10}")
    print("-" * 45)

    for name, data in gradebook.items():
        print(f"{name:<20}{data['score']:<12.1f}{data['weight']:<10.1f}%")

    print("-" * 45)
    print(f"Final Weighted Score: {final_score:.2f}%")
    print(f"Final Letter Grade:   {letter_grade}")
    print("=" * 45)


def main():
    grades = collect_assignments()
    final_score, letter_grade = calculate_final_grade(grades)
    display_report(grades, final_score, letter_grade)


if __name__ == "__main__":
    main()