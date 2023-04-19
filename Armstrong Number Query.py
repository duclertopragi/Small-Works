print("This is a Armstrong Number Query")
print("Please input numbers bigger than 9")

while True: # Prompt the user to input the range
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    if start > 9 and end > 9:
        break
    else:
        print("Invalid input. Both numbers must be greater than 9.")

def is_armstrong(num): # Define a function to check if a number is an Armstrong number
    
    num_str = str(num) # Convert the number to a string in order to count the number of digits
    
    n = len(num_str) # Get the number of digits
    
    sum = 0 # Compute the sum of the cubes of the digits
    for digit in num_str:
        sum += int(digit)**n
    
    return sum == num # Check if the sum is equal to the original number

# Check each number in the range for Armstrong number and store in a list
armstrong_nums = []
for num in range(start, end+1):
    if is_armstrong(num):
        armstrong_nums.append(num)

# Print the list of Armstrong numbers
print("The Armstrong numbers in the range", f"{start:,d}", "to", f"{end:,d}", "are:")
if armstrong_nums == []:
    print("There is no Armstrong number that you have inputed...")

    for j in armstrong_nums:
        print("{:,}".format(j))