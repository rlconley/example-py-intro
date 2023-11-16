def get_user_numbers():
    '''asks user to input two numbers and returns those numbers as a tuple'''
    # convert user input from string to integer
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    # str() would convert the values back to strings
    return a, b
    # this structure is called a tuple, can return multiple values separated by commas


def compare_numbers(a, b):
    '''takes in two numbers and prints to console whether a > b, a < b, or a == b'''
    print("The first number is ", a, "and the second number is ",
          b, "and their sum is ", a + b)

    if a > b:
        print(a, "is greater than ", b)
    elif a < b:
        print(a, "is less than ", b)
    elif a == b:
        print(a, "equals ", b)


def get_and_compare_numbers():
    # compare_numbers(get_user_numbers())
    # we can split this up into two lines
    first_num, second_num = get_user_numbers()
    # this is called unpacking a tuple, where we assign values to each item in the tuple
    print("The first number is ", first_num,
          "and the second number is", second_num)
    # capture the numbers returned by get_user_numbers()
    compare_numbers(first_num, second_num)
    # pass those numbers as input to compare_numbers


get_and_compare_numbers()

# # say hi 5 times
# count = 0
# while count < 5:
#     print("Hi!", count)
#     count += 1
