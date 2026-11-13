# %% 1. Create variables to store a student's name, age, and exam score. Print all three values.
from pydantic import validate_call

@validate_call(config={"strict": True})
def student_data(name: str, age: int, score: int) -> None:
    print("Student Name:", name)
    print("Student Age:", age)
    print("Exam Score:", score)
    
student_data("Purabi Das", 20, 85)



# %% 2. Create two integer variables, add them, and print the result.
a = 10
b = 20
result = a + b
print("Result:", result)



# %% 3. Store a model accuracy of 0.95 in a variable and print its data type using type().
model_accuracy = 0.95
print("Data Type of model accuracy:", type(model_accuracy))



# %% 4. Take a number as input from the user and print its square.
num = int(input("Enter a number: "))
print("Square of the number:", num ** 2)



# %% 5. Convert the string "100" into an integer and add 50 to it.
num = "100"
converted_num = int(num)
result = converted_num + 50
print("Result after adding 50:", result)



# %% 6. Convert 25 into a float and print the result.
num = 25
print("Float value of 25: ", float(num))



# %% 7.  Write a program to calculate the sum, difference, product, and division of two numbers.
def calculate_operations(num1: float, num2: float) -> None:
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
    print("Sum:", sum)
    print("Difference:", difference)
    print("Product:", product)
    print("Division:", division)
    
calculate_operations(10, 10)



# %% 8. Take a student's marks as input and check whether the student scored at least 40 marks.
student_marks = int(input("Enter student's marks:"))
if student_marks >= 40:
    print("The sudent has passed!")
else:
    print("The student has failed!")



# %% 9. Take a number as input and check whether it is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    
    
# %% 10. Take a student's marks and print Pass if marks are at least 40; otherwise print Fail.
marks = int(input("Enter the marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")



# %% 11. Check whether a given age is between 18 and 60 using comparison and logical operators.
age = int(input("Enter the age:"))
if 18 <= age <= 60:
    print("The age is between 18 and 60.")
else:
    print("The age is not between 18 and 60.")



# %% 12.  Print the numbers from 1 to 10 using a for loop and range().
for i in range(1, 11):
    print(i)



# %% 13. . Print all even numbers from 2 to 20 using a for loop.
for i in range(2, 21, 2):
    print(i)



# %% 14. Calculate the sum of numbers from 1 to 10 using a loop.
sum = 0
for i in range(1, 11):
    sum+= i
print(sum)



# %% 15. . Print the multiplication table of a number entered by the user.
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



# %% 16. Use a while loop to print the numbers from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1



# %% 17. Write a function named calculate_sum() that accepts two numbers and returns their sum.
def calculate_sum(num1: float, num2: float) -> float:
    return num1 + num2

calculate_sum(10, 20)



# %% 18. Write a function named check_pass() that accepts marks and returns "Pass" or "Fail".
def check_pass(marks: int) -> str:
    return "Pass" if marks >= 40 else "Fail"

check_pass(50)



# %% 19. Create a lambda function that squares a number and call it with 5.
square = lambda x: x ** 2
print(square(5))



# %% 20. Write a function that accepts a number and prints it. Demonstrate the difference between a parameter and an argument.
def print_number(num: int) -> None:
    print("The number is:", num)
print_number(10)  # 10 is the argument passed to the function




# %% 21. Take three model accuracy scores as input and print the highest score using if/elif/else.
score1 = float(input("Enter the first model accuracy score: "))
score2 = float(input("Enter the second model accuracy score: "))    
score3 = float(input("Enter the third model accuracy score: "))

if score1 >= score2 and score1 >= score3:
    print("The highest score is:", score1)
elif score2 >= score3:
    print("The highest score is:", score2)
else:
    print("The highest score is:", score3)
    
    
    
# %% 22. Take a model's accuracy and training time as inputs. Print "Good Model" if accuracy is at least 0.90 and training time is at most 60 minutes; otherwise print "Needs Improvement".
accuracy = float(input("Enter the model's accuracy: "))
training_time = float(input("Enter the model's training time (in minutes): "))

if accuracy >= 0.90 and training_time <= 60:
    print("Good Model")
else:
    print("Needs Improvement")
    
    

# %% 23. Take a temperature value as input. Print "Low" below 20, "Normal" from 20 to 35 inclusive, and "High" above 35.
temp = float(input("Enter the temperature value: "))
if temp < 20:
    print("Low")    
elif 20 <= temp <= 35:
    print("Normal")
else:
    print("High")
    


# %% 24. Print the numbers from 1 to 30, but skip numbers divisible by 3 using continue.
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)



# %% 25. Print numbers from 1 onward using a while loop and stop when the number reaches 10 using break.
i = 1
while True:
    if i > 10:
        break
    print(i)
    i += 1  
    

# %% 26. Calculate the factorial of a positive integer using a for loop.
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
factorial(5)    



# %% 27. Count how many numbers between 1 and 50 are divisible by both 3 and 5.
count = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print(count)



# %% 28. Take 10 model scores as input using a loop and calculate their average. Do not use lists.
total = 0
for i in range(10):
    score = float(input(f"Enter the model score {i+1}:"))
    total += score
average = total / 10
print("Average model score:", average)




# %% 29. Write a function calculate_accuracy(correct, total) that returns the accuracy as correct / total. Handle total equal to zero using a condition.
def calculate_accuracy(correct: int, total: int) -> float:
    if total == 0:
        return 0.0
    return correct/total

calculate_accuracy(8, 10)



# %% 30. Write a function that accepts a score and returns "Excellent", "Good", or "Poor" using if/elif/else.
def evaluate_score(score: float) -> str:
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"   
    else:
        return "Poor"
    
evaluate_score(85)



# %% 31. Write a function with a default parameter for the learning rate, set to 0.01, and print the supplied values.
def print_learning_rate(learning_rate: float = 0.01) -> None:
    print("Learning Rate:", learning_rate)

print_learning_rate()  # Uses default value
print_learning_rate(0.05)  # Uses supplied value



# %% 32. Write a function that accepts a number and returns True if it is even and False otherwise.
def is_even(num: int) -> bool:
    return num % 2 == 0

is_even(4)  # Returns True
is_even(5)  # Returns False



# %% 33. Create a global variable named learning_rate. Access it inside a function and print its value.
learning_rate = 0.01

def global_learning_rate():
    global learning_rate
    print("Global Learning Rate:", learning_rate)
    
global_learning_rate()  # Accesses and prints the global variable



# %% 34. Create a global variable named score. Inside a function, create a local variable with the same name and demonstrate which value is printed inside and outside the function.
score = 85  
def local_score():
    score = 90
    print("Local Score inside function:", score)
    
local_score()  # Prints local score
print("Global Score outside function:", score)  # Prints global score




# %% 35. Write a function that accepts any number of scores using *args and returns their average. Handle the case when no scores are provided.
def average_score(*args: float) -> float:
    if not args:
        return 0.0
    return sum(args) / len(args)

print(average_score(80, 90, 70))  # Returns average of provided scores
print(average_score())  # Returns 0.0 when no scores are provided



# %% 36. Write a function using **kwargs to accept named model settings such as learning_rate=0.01 and epochs=10. Print the received settings.
def model_settings(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

model_settings(learning_rate=0.01, epochs=10)




# %% 37. Write a function that accepts a required model name and any number of additional positional arguments using *args. Print the name and each additional argument.
def model_info(model_name: str, *args):
    print("model Name:", model_name)
    for arg in args:
        print("Additional Argument:", arg)
        
model_info("Random Forest", "max_depth=10", "n_estimators=100")



# %% 38. Create a lambda function that accepts two numbers and returns the larger one using a conditional expression.
larger_number = lambda x, y: x if x > y else y
print(larger_number(10, 20)) 




# %% 39. Write a decorator that prints "Starting calculation" before calling a function, then demonstrate it on a function that adds two numbers.
def print_starting(func):
    def wrapper(*args, **kwargs):
        print("Starting calculation")
        return func(*args, **kwargs)
    return wrapper

@print_starting
def add_numbers(x, y):
    return x + y

print(add_numbers(5, 10))



# %% 40. Write a function that accepts a number and a function as arguments. Apply the supplied function to the number and return the result. Demonstrate it using a lambda function.
def apply_function(num: float, func) -> float:
    return func(num)

result = apply_function(5, lambda x: x ** 2)
print(result)  # Prints 25

# %% 41. Write a program that accepts the actual value and predicted value of a model. Calculate the absolute error using conditions and arithmetic operators.
def calculate_absolute_error(actual, predicted):
    absolute_error = abs(actual - predicted)
    return absolute_error

actual_value = 10
predicted_value = 7
error = calculate_absolute_error(actual_value, predicted_value)
print("Absolute Error:", error)




# %% 42. Take 10 prediction errors as input using a loop. Calculate and print their mean absolute error (MAE) without using lists or libraries.
total_error = 0.0
for i in range(10):
    error = float(input(f"Enter prediction error {i + 1}: "))
    total_error += abs(error)

mae = total_error / 10
print("Mean Absolute Error:", mae)


# %% 43. Take 10 actual values and 10 predicted values, one pair at a time. Calculate the mean squared error (MSE) using a loop.
total_squared_error = 0.0
for i in range(10):
    actual = float(input(f"Enter actual value {i + 1}: "))
    predicted = float(input(f"Enter predicted value {i + 1}: "))
    squared_error = (actual - predicted) ** 2
    total_squared_error += squared_error

mse = total_squared_error / 10
print("Mean Squared Error:", mse)



# %% 44. Write a function calculate_mae(error1, error2, error3) that returns the average absolute error for three predictions.
def calculate_mae(error1: float, error2: float, error3: float) -> float:
    return (abs(error1) + abs(error2) + abs(error3)) / 3

print(calculate_mae(2.5, -3.0, 1.5))  



# %% 45. Write a function that accepts correct predictions and total predictions, calculates accuracy, and classifies the model as "Excellent" (at least 95%), "Good" (at least 85%), or "Needs Improvement".
def classify_model(correct: int, total: int) -> str:
    if total == 0:
        return "No predictions made"
    
    accuracy = (correct / total) * 100
    
    if accuracy >= 95:
        return "Excellent"
    elif accuracy >= 85:
        return "Good"
    else:
        return "Needs Improvement"
    
classify_model(90, 100)  




# %% 46. Simulate training for 20 epochs using a loop. Start with a loss value of 1.0 and reduce it by 0.05 each epoch. Stop early using break when the loss reaches 0.20 or lower.
loss = 1.0
for epoch in range(20):
    print(f"Epoch {epoch + 1}: Loss = {loss}")
    loss -= 0.05
    if loss <= 0.20:
        print("Early stopping triggered.")
        break


# %% 47. Simulate 15 training epochs. Skip reporting for every epoch divisible by 3 using continue, and print the remaining epoch numbers and loss values.
loss = 1.0
for epoch in range(15):
    if epoch % 3 == 0:
        continue
    print(f"Epoch {epoch + 1}: Loss = {loss}")
    loss -= 0.05
    

# %% 48. Write a function that accepts a starting loss, a reduction amount, and a number of epochs. Use a loop to calculate the final loss and return it.
def final_loss(starting_loss: float, reduction: float, epochs: int) -> float:
    loss = starting_loss
    for _ in range(epochs):
        loss -= reduction
    return loss

final_loss_value = final_loss(1.0, 0.05, 10)
print("Final Loss after 10 epochs:", final_loss_value)



# %% 49. Create a function calculate_score(value, multiplier=1) that returns value multiplied by the multiplier. Demonstrate calls with and without the optional argument.
def calculate_score(value: float, multiplier: float = 1) -> float:  
    return value * multiplier

# Demonstrate calls with and without the optional argument
print(calculate_score(10.0))        # Uses default multiplier (1)
print(calculate_score(10.0, 2.0))    # Uses provided multiplier (2)



# %% 50. Write a function that accepts any number of model scores using *args and returns the highest score without using lists or built-in maximum functions.
def highest_score(*args):   
    if not args:
        return None  # Return None if no scores are provided
    
    max_score = args[0]  # Initialize max_score with the first argument
    for score in args:
        if score > max_score:
            max_score = score  # Update max_score if a higher score is found
    return max_score

# Demonstrate the function
print(highest_score(85, 90, 78, 92, 88))



# %% 51. Write a function that accepts any number of validation scores using *args and returns their average. Then use it to compare two model averages with a conditional statement.
def average_score(*args):
    if not args:
        return 0.0  # Return 0.0 if no scores are provided
    return sum(args) / len(args)  # Calculate and return the average

# Demonstrate the function  
print(average_score(85, 90, 78, 92, 88))



# %% 52. Write a function that accepts model settings through **kwargs. Use conditions to print the learning rate and number of epochs when those named arguments are supplied. Do not use dictionaries or other untaught concepts explicitly.
def print_model_settings(**kwargs):
    if 'learning_rate' in kwargs:
        print("Learning Rate:", kwargs['learning_rate'])
    if 'epochs' in kwargs:
        print("Number of Epochs:", kwargs['epochs'])

print_model_settings(learning_rate=0.001, epochs=100)



# %% 53. Write a function that accepts *args and **kwargs together. Print the positional values and the named model settings separately.
def print_args_kwargs(*args, **kwargs):
    print("Positional Arguments:")
    for arg in args:
        print(arg)
    
    print("\nNamed Model Settings:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
# Demonstrate the function
print_args_kwargs("Model A", "Model B", learning_rate=0.01, epochs=10)  




# %% 54. Create a global variable training_status = "Not Started". Write a function that changes it to "Completed" using the global keyword. Print the value before and after calling the function.
training_status = "Not Started"

def complete_training():
    global training_status
    training_status = "Completed"

print("Before:", training_status)
complete_training()
print("After:", training_status)



# %% 55. Write a decorator that prints "Training started" before a function executes and "Training finished" after it executes. Apply it to a function that prints the current epoch.
def training_decorator(func):
    def wrapper(*args, **kwargs):
        print("Training started")
        result = func(*args, **kwargs)
        print("Training finished")
        return result
    return wrapper  

@training_decorator
def print_epoch(epoch):
    print("Current Epoch:", epoch)

print_epoch(5)




# %% 56. Write a decorator that accepts a function, executes it, and returns its result. Demonstrate it using a function that calculates model accuracy.
def accuracy_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper  

def calculate_accuracy(correct, total):
    if total == 0:
        return 0.0
    return (correct / total) * 100

calculate_accuracy = accuracy_decorator(calculate_accuracy)
print(calculate_accuracy(85, 100))




# %% 57. Create a lambda function that calculates squared error from actual and predicted values. Use it inside a regular function to calculate the total squared error for three predictions.
squared_error = lambda actual, predicted: (actual - predicted) ** 2

def calculate_total_squared_error(*predictions):
    total_error = 0
    for actual, predicted in predictions:
        total_error += squared_error(actual, predicted)
    return total_error

print(calculate_total_squared_error((85, 80), (90, 95), (78, 82)))



# %% 58. Write a function that accepts a threshold and a model score. Return "Accept" when the score is greater than or equal to the threshold and "Reject" otherwise. Use a default threshold of 0.90.
def evaluate_model(threshold: float = 0.90, score: float = 0.0) -> str:
    return "Accept" if score >= threshold else "Reject"

print(evaluate_model(score=0.95))
print(evaluate_model(score=0.85))



# %% 59. Simulate model evaluation for 10 predictions. Take actual and predicted values one pair at a time, count correct predictions, and calculate accuracy. Use a function for the evaluation and a loop for the repeated inputs.
actual_values = [0.95, 0.85, 0.92, 0.88, 0.90, 0.87, 0.93, 0.89, 0.91, 0.86]    
predicted_values = [0.90, 0.80, 0.88, 0.92, 0.85, 0.90, 0.88, 0.95, 0.85, 0.90]
correct_predictions = 0

evaluate_model = lambda score: "Accept" if score >= 0.90 else "Reject"

for actual, predicted in zip(actual_values, predicted_values):
    if evaluate_model(score=actual) == "Accept" and evaluate_model(score=predicted) == "Accept":
        correct_predictions += 1

accuracy = (correct_predictions / len(actual_values)) * 100
print("Accuracy:", accuracy)



# %% 60. Build a mini training simulation using functions, a decorator, a loop, conditions, break, and a lambda function. Print the loss for each epoch, stop when loss reaches 0.10 or lower, and return the final loss. Use only the Python concepts covered in class.
def training_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@training_decorator
def print_loss(loss):
    print("Current Loss:", loss)

loss = 1.0
while loss > 0.10:
    loss *= 0.9  # Simulate loss reduction
    print_loss(loss)

print("Final Loss:", loss)

