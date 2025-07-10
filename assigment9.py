num = input("give me a number: ")
int_num = int(num)
while(int_num>0):
    int_num= int_num -1
    if int_num % 3 == 0 and int_num % 5 == 0:
        print("fizzbuzz" , int_num)
    elif int_num % 3 == 0:
        print("fizz" , int_num)
    elif int_num % 5 == 0:
        print("buzz" , int_num)
    else:
        print("wow", int_num) 