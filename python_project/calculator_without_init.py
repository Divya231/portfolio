class Calculator:
    def Addition(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("ADDITION OF TWO NUMBER ARE: ")
        return self.num1+self.num2
    def Subtraction(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("SUBTRACTION OF TWO NUMBERS ARE : ")
        return self.num1-self.num2
    def Multiplication(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("MULTIPLICATION OF TWO NUMBERS ARE: ")
        return self.num1*self.num2
    def Division(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("DIVISION OF TWO NUMBERS ARE : ")
        return self.num1/self.num2
    def Square(self,num):
        self.num=num
        print("SQUARE OF A NUMBER IS : ")
        return self.num*self.num
if __name__ == '__main__':
            num1=int(input("enter a number1: "))
            num2=int(input("enter a number2: "))
            Calculator=Calculator() 
while True:
    print("\nWELCOME TO CALCULATOR\n PLEASE CHOOSE AN OPTION: \n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.SQUARE\n6.EXIT")
    a=int(input("Enter your choice : "))
    if a==1:
        print(Calculator.Addition(num1,num2))
    elif a==2:
        print(Calculator.Subtraction(num1,num2))
    elif a==3:
        print(Calculator.Multiplication(num1,num2))
    elif a==4:
        print(Calculator.Division(num1,num2))
    elif a==5:
        print(Calculator.Square(num1))
    elif a==6:
        print("THANKU FOR USING THE CALCULATOR...")
        exit()
    else:
        print("INVALID CHOICE")
    