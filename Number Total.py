No1 = int(input("Please Enter your first number: "))
No2 = int(input("Please Enter your second number: "))


def numberTotal(N1,N2):
    global total
    total = 0
    for x in range(N1,N2):
        total = total + x
    print("The total of the numbers is",total)

numbertotal(No1,No2)


    
    
