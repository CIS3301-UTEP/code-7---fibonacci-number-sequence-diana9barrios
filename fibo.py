def get_fibonacci_number(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    previous_a = 0 
    previous_b = 1

    for x in range(2,number+1):
        current_fibo_number = previous_a + previous_b
        previous_a = previous_b
        previous_b = current_fibo_number

    return previous_b


def get_fibonacci_sequence(n):
    if n == 0:
        return[0]
    if n == 1:
        return[0,1]
    previous_x = 0 
    previous_y = 1

    number_sequence = [0,1]

    for i in range(2, n+1):
        current = previous_x + previous_y
        previous_x = previous_y
        previous_y = current

        number_sequence.append(current)
    return number_sequence
print(get_fibonacci_sequence(5))
print(get_fibonacci_number(4))