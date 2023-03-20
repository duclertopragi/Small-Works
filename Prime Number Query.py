# at the 10th line program: why "int(num/2)+1"?
# I think it should be just "num" I modified it at below
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers between", start, "and", end, "are: ")

for num in range(start, end+1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            print(num)


# This is the algo should be
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers between", start, "and", end, "are: ")

for num in range(start, end+1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            
# And lastly this is the I wrote
# but I was planning to add a while loop for checking
# bigger/lower number between 38th line and 40th line

print("This is a listing prime numbers within given range program")    

nr1 = int(input("Please indicate the lowest number: "))
nr2 = int(input("Please indicate the highest number: "))

for n in range(nr1, nr2+1):
    if n > 1:
        for i in range(2,n):
            if (i % n == 0):
                print(n, "is not a prime number")
            else:
                print(n, "is a prime number")