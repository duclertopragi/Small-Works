print("""
      **********************************************************************
      
      **** This is a prime number listing program within a given range *****
      
      **********************************************************************
""")

while True:
    
    num1 = int(input("Please indicate the lowest number: "))
    num2 = int(input("Please indicate the highest number: "))
    
    if num2 < num1:
        print("You have entered numbers incorrectly")
        continue
    else:
    
               for j in range(num1, num2+1):
                   if j > 1:
                       for i in range(2, int(j/2)+1): # Attention! Attention! This is a sharp expression: "int(j/2)+1". There is no need to look for a divider after the half the number cos there can't be any more divider after the half of it...
                           if (j % i == 0):
                               break
                       else:
                           print(j, "is a prime number")
