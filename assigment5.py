num1 = input("give me a number: ")
num2 = input("give us second number: ")
int_num1 = int(num1)
int_num2 = int(num2)

func = input("what do you wanna do? ")
if func == "add":
    print(int_num1 + int_num2)
elif func == "multiply":
    print(int_num1 * int_num2)
elif func == "divide":
    if int_num2 == 0:
        print("try again boy")
    print(int_num1 / int_num2)

elif func == "subtract":
    print(int_num1 - int_num2)

else:
    print("Invalid operation")
    print(result) 
    



