# Q2: Count Even and Odd Numbers

nums = input("Enter numbers separated by commas: ")

numbers = [int(x) for x in nums.split(",")]

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Printing results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
