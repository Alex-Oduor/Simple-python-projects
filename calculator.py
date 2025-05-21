
choice='Y'
while choice=='Y':
 print("***Simple Calculator***\n")
       
 num1=int (input("Enter the first number:"))
 num2=int (input("Enter the second number: "))
 operation= input("Choose one operation [+,/,*,-]: ")


 for sign in operation:
    if sign == '+':
            results= num1+num2
            print("The sum is: ",results)
            break
    elif sign =='-':
           results= num1-num2
           print("The answer is: ",results)
           break
    elif sign =='/':
            if num2==0 :
                  print("Error cannot divide by zero")
                  break
            else:
                 results= num1/num2
                 print("The answer is: ",results)
                 break
    elif sign =='*':
            results= num1*num2
            print("The answer is: ",results)
            break
    else: print("Invalid input!! please try again.")

 choice=input("\nWould you like to perform another operation?[Y/N]: ")
 choice=choice.upper()
print("Thank you...exiting the program")

        



