# List perfect number(s) within given range

print("""
***** This is a perfect number query. *****\n
You need to input 'starting' and 'ending' of the range in order to run the query.
""")

while True:
          
    start = int(input("Please indicate the lowest figure in your range: "))
    end = int(input("Please indicate the highest figure in your range: "))
    
    if start < 0 or end < 0:
        print("You've typed in incorrect figures, please input positive integers")
        continue
    
    perfect_numbers = []
    
    for num in range(start, end+1):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            perfect_numbers.append(num)
    
    if perfect_numbers:
        print("Perfect numbers between", start, "and", end, "are:", perfect_numbers)
    else:
        print("There are no perfect numbers between", start, "and", end)
        
    break