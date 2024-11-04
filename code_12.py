def get_fibonacci_number(position):
    # pass #Remove this line and insert your code here. Do not forget this function implements recursion.
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fibonacci_number(position-1)+get_fibonacci_number(position-2)

def get_fibonacci_number_sequence(number):
    # pass #Remove this line and insert your code here. Do not forget to use get_fibonacci_number to create your list of numbers.
    if number == 0:
        return [0]
    elif number == 1:
        return [0,1]
    prev1 = 0
    prev2 = 1
    number_sequence = [0,1]
    for i in range(2, number + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
        number_sequence.append(current)
    return number_sequence

   
       
if __name__ == "__main__":
    # pass #Remove this line and insert your code to test your Fibonacci function here
    result_a = get_fibonacci_number(2)
    print (result_a)
    result_b = get_fibonacci_number_sequence(5)
    print (result_b)