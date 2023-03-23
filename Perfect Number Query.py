# List perfect number(s) within given range

print("""
***** This is a perfect number query. *****\n
You need to input 'starting' and 'ending' of the range in order to run the query.
""")

nb1 = int(input("Enter the starting number of the range: ")) 
nb2 = int(input("Enter the ending number of the range: "))

for n in range (nb1, nb2+1):
    smm = 0
    for i in range(1,n):
        if n % i == 0:
          smm += i

    if n == smm:
        print(n)