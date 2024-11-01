#Your code goes here. 

import math
def main():
    a = input("first number")
    b = input("second number")

def safe_divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")

def process_list(input_list):
        for x in range(len(input_list)):
            try:
                input_list[x] = input_list[x] * 3
            except TypeError and ValueError:
                print("invalid input")

def nested_operations(a, b):
    try: 
        print(a / b)
        try: 
            print(math.sqrt(a/b)) 
            return "whoKnowsWhat"
        except ZeroDivisionError: 
            return "Its Very Broken"
    except ZeroDivisionError: 
        return "Its Broken"


def process_input():




main()
