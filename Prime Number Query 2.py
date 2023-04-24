# This is much more advanced version of the first edition.
# Mathematically and structurally I took this simple function one step futher

def Find_Prime(start, end):
    list_of_primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(num**(0.5))+1):
                if num%i == 0:
                    break
            else:
                list_of_primes.append(num)
    return list_of_primes

start = int(input("Please indicate starting range: "))
end = int(input("Please indicate the ending of the range: "))

print(f"Prime numbers in the range of {start} to {end} are: {Find_Prime(start, end)}")