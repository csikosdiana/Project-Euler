'''
Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain
with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''


def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def create_factorial_dictionary():
    factorials_dictionary = {}
    for i in range(10):
        factorials_dictionary[i] = factorial(i)
    return factorials_dictionary


factorials_dictionary = create_factorial_dictionary()

chains_with_sixty_terms = 0

for i in range(2, 1000000):
    seen_numbers = {i: ''}
    current_number = i
    while True:
        if len(seen_numbers) == 60:
            chains_with_sixty_terms += 1
            break
        next_number = sum([factorials_dictionary[int(n)] for n in str(current_number)])
        if next_number in seen_numbers:
            break
        seen_numbers[next_number] = ''
        current_number = next_number

		
print(chains_with_sixty_terms)  # 402
