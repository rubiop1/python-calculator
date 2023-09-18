from Calculate.calculator import Operations

operator = Operations(0)
global val1, val2
choice = 1

def read():
   global val1, val2
   val1 = int(input("Enter first numbers: "))
   val2 = int(input("Enter a second number: "))


while choice >= 1 or choice <= 6:
    print("1. addition +")
    print("2. subtraction -")
    print("3. multiplication *")
    print("4. division /")
    print("5. exponent ^")
    print("6. exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        read()
        print("Addition = " + str(operator.add(val1, val2)))
        choice = 0
    elif choice == 2:
        read()
        print("Substraction = " + str(operator.less(val1, val2)))
        choice = 0
    elif choice == 3:
        read()
        print("multiplication = " + str(operator.times(val1, val2)))
        choice = 0
    elif choice == 4:
        read()
        print("division = " + str(operator.div(val1, val2)))
        choice = 0
    elif choice == 5:
        read()
        print("exponent = " + str(operator.exp(val1, val2)))
        choice = 0
    elif choice == 6:
        print("Bye... Thanks for playing")
        exit()