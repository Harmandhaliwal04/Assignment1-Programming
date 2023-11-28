def takeInput():
    a=int(input("Enter the number one="))
    b=int(input("Enter the number two="))
    c =input("Enter the operator")
    displayresult(a,b,c)

def displayresult(a,b,c):
        if c=="+":
                Add(a,b)
        elif c=="-":
            sub(a,b)
        elif c=="*":
            multi(a,b)
        elif c=="/":
            Divide(a,b)
        else:
            print("Invalid Operator")
   


def Add(a,b):
    d=a+b
    print(d)
 
def sub(a,b):
    d=a-b
    print(d)

def multi(a,b):
    d=a*b
    print(d)

def Divide(a,b):
    d=a/b
    print(d)

takeInput()




