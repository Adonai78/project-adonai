num = input("give me a number: ")
int_num = int(num)
if int_num % 3 == 0 and int_num % 5 == 0:
    print("fizzbuzz")
elif int_num % 3 == 0:
    print("fizz")
elif int_num % 5 == 0:
    print("buzz")
else:
    print("wow")