# List Comprehension Practice

# Lesson 25: Advanced Python Functions
# Perform List Comprehension to get mentioned results.

num = int(input("Enter a number: "))

odd_numbers = [i for i in range(num) if i % 2 != 0]
another_odd_list = [i for i in odd_numbers]  

print("Odd numbers under", num, ":", odd_numbers)
print("Another list of odd numbers:", another_odd_list)

fruits = ["apple", "banana", "cherry", "mango"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated fruit list:", capitalized_fruits)
