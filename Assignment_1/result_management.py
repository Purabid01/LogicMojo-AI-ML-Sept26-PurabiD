# QS: 1
# Scenario: You are building a simple student result management system. Write a Python program that performs the following tasks:

# Ask the user to enter marks for 5 students using a while loop.
# If the entered marks are outside the range of 0–100, display an invalid marks message and skip that entry using continue. The user must still enter marks until 5 valid entries have been collected.
# Use a for loop to process the collected marks.
# If marks are 90 or above, print Grade A.
# If marks are between 75 and 89, print Grade B.
# If marks are between 60 and 74, print Grade C.
# If marks are between 40 and 59, print Pass.
# Otherwise, print Fail.
# If marks are exactly 0, use break to stop processing further students.
# Include a pass statement as a placeholder for a future feature, such as saving student results to a file.
# Finally, print how many valid marks were collected.



valid_marks = []

while len(valid_marks) < 5:
    score = int(input("Enter marks for student (0-100): "))
    
    if score < 0 or score > 100:
        print("Invalid marks. Please enter a value between 0 and 100.")
        continue
    
    valid_marks.append(score)
    
print("Total valiid marks collected:", len(valid_marks))

for marks in valid_marks:
    if marks == 0:
        print("Processing stopped due to a score of 0.")
        break
    
    if marks >= 90:
        print(f"Marks: {marks} - Grade A")
    elif marks >= 75:
        print(f"Marks: {marks} - Grade B")
    elif marks >= 60:
        print(f"Marks: {marks} - Grade C")
    elif marks >= 40:
        print(f"Marks: {marks} - Pass")
    else:
        print(f"Marks: {marks} - Fail")

    # placeholder for future feature
    pass


