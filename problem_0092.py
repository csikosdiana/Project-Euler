'''
Square digit chains

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''


from itertools import permutations

def square_digit_chains(n):
    ends_with_1 = {1: 1}
    ends_with_89 = {}
    count_where_ends_with_89 = 0
    for i in range(2, n):

        numbers_in_chain = []
        current_number = i

        if current_number in ends_with_1:
            continue
        elif current_number in ends_with_89:
            count_where_ends_with_89 +=1
            continue

        while True:
            next_number = sum([int(n)**2 for n in str(current_number)])
            next_number_permutations = list(permutations(list(str(current_number))))
            next_numbers = [int(''.join(i)) for i in next_number_permutations]
            numbers_in_chain += next_numbers

            if next_number == 1 or next_number in ends_with_1:
                for value in numbers_in_chain:
                    ends_with_1[value] = 1
                break
            elif next_number == 89 or next_number in ends_with_89:
                for value in numbers_in_chain:
                    ends_with_89[value] = 89
                count_where_ends_with_89 +=1
                break

            current_number = next_number

    return count_where_ends_with_89


print(square_digit_chains(10000000))  # 8581146
