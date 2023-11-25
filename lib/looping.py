#!/usr/bin/env python3

def happy_new_year():
    count = 10
    
    while count > 0:
        print(count)
        count -= 1
    
    print("Happy New Year!")

# Call the function
happy_new_year()

    
def square_integers(int_list):
    square_integers = [x * x for x in int_list]
    return square_integers

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function
fizzbuzz()

        
