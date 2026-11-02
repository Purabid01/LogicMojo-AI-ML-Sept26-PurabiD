# QS: 2
# Create a BMI (Body Mass Index) Calculator using Python. Your program should demonstrate conditional statements, loops and loop-control statements without using lists or membership operators. Requirements

# Use a while loop to allow the user to calculate BMI for multiple people.
# Ask the user to enter their weight in kilograms and height in metres.
# If the weight or height is zero or negative, display an invalid-input message and use continue to ask again.
# Calculate BMI using the formula: BMI = weight (kg) ÷ height (m)²
# Use if-elif-else to classify BMI:
# Below 18.5: Underweight
# 18.5 to below 25: Normal weight
# 25 to below 30: Overweight
# 30 or above: Obesity range
# Use a nested if to provide an additional message for people in the normal BMI range.
# Use if-else to check whether BMI is below 25.
# Use break to stop the program when the user enters 0 as their weight.
# Use a for loop to display a countdown from 3 to 1 before exiting.
# Use pass as a placeholder for a future feature.



people_count = int(input("Enter the number of people to calculate BMI for: "))

if people_count <= 0:
    print("Invalid input. Number of people must be a positive integer.")
    
exit_flag = False

while people_count > 0:
    weight = float(input("Enter weight in kilograms: "))
    if weight == 0:
        print("Weighted input is zero. Exiting the program.")
        exit_flag = True
        break
    if weight < 0:
            print("Invalid input. Weight must be a positive number. Please type a valid input.")
            continue
        
    height = float(input("Enter height in metres: "))
    if height <= 0:
        print("Invalid input. Height must be a positive number. Please type a valid input.")
        continue
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        print(f"BMI: {bmi:.2f} - Underweight")
    elif bmi < 25:
        print(f"BMI: {bmi:.2f} - normal weight")
        if bmi < 25:
            print("You are in the normal BMI range.")
    elif bmi < 30:
        print(f"BMI: {bmi:.2f} - overweight")
    else:
        print(f"BMI: {bmi:.2f} - obesity")
        
    pass  # Placeholder for future feature

    people_count -= 1

if not exit_flag and people_count == 0:
    print("All BMI calculations completed.")

   
for i in range(3, 0, -1):
    print(f"Exiting in {i}...")
print("Program Finished.")

