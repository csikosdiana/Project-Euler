'''
Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down,
is indicated in bold red and is equal to 2427.

                                                131  673  234  103   18
                                                201   96  342  965  150
                                                630  803  746  422  111
                                                537  699  497  121  956
                                                805  732  524   37  331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
'''


def minimal_path_sum_two_ways(filename):
    result = []

    for line in list(open(filename)):
        numbers = list(map(int, line.rstrip().split(',')))
        if not result:
            result.append(numbers[0])
            for i in range(1, len(numbers)):
               result.append(result[i - 1] + numbers[i])
            continue

        temporary_result = []

        temporary_result.append(result[0] + numbers[0])
        for i in range(1, len(numbers)):
            next_minimal = min(result[i], temporary_result[i - 1])
            temporary_result.append(next_minimal + numbers[i])

        result = temporary_result
    
    return result[-1]



print(minimal_path_sum_two_ways("problem_0081_5x5.txt"))  # 2427
print(minimal_path_sum_two_ways("problem_0081_80x80.txt"))  # 427337
