
'''
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiples_of_3_and_5(max_limit):
    sum_of_all_multiples = 0

    for n in range(3, max_limit):
        if n % 15 == 0:
            sum_of_all_multiples += n
        elif n % 3 == 0 or n % 5 == 0:
            sum_of_all_multiples += n

    return sum_of_all_multiples


print(multiples_of_3_and_5(1000))  # 233168
