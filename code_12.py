def get_fibonacci_number(position):
    # pass #Remove this line and insert your code here. Do not forget this function implements recursion.
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        # formula fn=fn-1+fn-2
        for i in range(2, position + 1):
            return ((position-1)+(position-2))

def get_fibonacci_number_sequence(number):
    # pass #Remove this line and insert your code here. Do not forget to use get_fibonacci_number to create your list of numbers.
    if number == 0:
        return [0]
    elif number == 1:
        return [1]

if __name__ == "__main__":
    # pass #Remove this line and insert your code to test your Fibonacci function here
    result_a = get_fibonacci_number(2)
    print (result_a)