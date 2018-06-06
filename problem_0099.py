'''
Largest exponential

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''


from math import log


def largest_exponential(filename):
    max_line_index = 0
    max_value = 0
    for i, line in enumerate(list(open(filename))):
        numbers = list(map(int, line.rstrip().split(',')))
        value = numbers[1] * log(numbers[0], 10)
        if value > max_value:
            max_value = value
            max_line_index = i + 1

    return max_line_index


print(largest_exponential("problem_0099.txt"))  # 709
