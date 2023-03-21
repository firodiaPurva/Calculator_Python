

def add(a,b):

    print(a+b)

def sub(a,b):
    if a>b:
        print(a-b)
    else:
        print(b-a)
    
def mult(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

def calc(n):
    if n==1:
        add(first,second)
    elif n==2:
        sub(first,second)
    elif n==3:
        mult(first,second)
    elif n==4:
        div(first,second)
    else:
        print("Invalid Choice")
    

first = int(input("Enter the first number : "))
second = int(input("Enter the second number : "))
print("Welcome to the calculate game!! Hope you enjoy :)")
print("Please select the operations you wannna perform : \n 1. Add \n 2. Substraction \n 3. Multiplication \n 4. Devision")
ch = int(input("Enter your choice here : "))
calc(ch)
p = True
while (p==True):
    choice = input("Do you wanna continue??\n Enter 'y' if yes and to exit enter 'n': ")
    if choice=='y':
        print("Welcome to the calculate game!! Hope you enjoy :)")
        print("Please select the operations you wannna perform : \n 1. Add \n 2. Substraction \n 3. Multiplication \n 4. Devision")
        ch = int(input("Enter your choice here : "))
        calc(ch)
    elif choice =='n':
        p = False
        print("Thankyou for using Purva's Calculator!!")
    else :
        p = False
        print("Invalid Choice")
        print("See You Soon!!")
        exit()


    
    
    
    
    
