def main():
	print("Student Grade Analyzer")

	while True:
		try:
			grade_count = int(input("Enter your Grade: "))
			if grade_count > 0:
				break
			print("Please enter at least one grade.")
		except ValueError:
			print("Please enter a whole number.")

	grades = []
	for index in range(grade_count):
		while True:
			try:
				grade = float(input(f"Enter grade {index + 1}: "))
				if 0 <= grade <= 100:
					grades.append(grade)
					break
				print("Please enter a grade from 0 to 100.")
			except ValueError:
				print("Please enter a valid number.")

	average = sum(grades) / len(grades)
	highest_grade = max(grades)
	lowest_grade = min(grades)
	result = "PASS" if average >= 75 else "FAIL"

	print("\nResults")
	print(f"Grades: {grades}")
	print(f"Average: {average:.2f}")
	print(f"Highest grade: {highest_grade:.2f}")
	print(f"Lowest grade: {lowest_grade:.2f}")
	print(f"Status: {result}")


if __name__ == "__main__":
	main()
