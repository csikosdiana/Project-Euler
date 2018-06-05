'''
Triangle containment

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

                                        A(-340,495), B(-153,-910), C(835,-947)

                                        X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles,
find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
'''


sign = lambda n: (n > 0) - (n < 0)


def is_contains_origo(points):
    AB_vector = (points[2] - points[0], points[3] - points[1])
    AO_vector = (0 - points[0], 0 - points[1])

    AB_AO_cross_product = AB_vector[0] * AO_vector[1] - AB_vector[1] * AO_vector[0]

    BC_vector = (points[4] - points[2], points[5] - points[3])
    BO_vector = (0 - points[2], 0 - points[3])

    BC_BO_cross_product = BC_vector[0] * BO_vector[1] - BC_vector[1] * BO_vector[0]

    if sign(AB_AO_cross_product) != sign(BC_BO_cross_product):
        return False

    CA_vector = (points[0] - points[4], points[1] - points[5])
    CO_vector = (0 - points[4], 0 - points[5])

    CA_CO_cross_product = CA_vector[0] * CO_vector[1] - CA_vector[1] * CO_vector[0]

    if sign(AB_AO_cross_product) == sign(BC_BO_cross_product) == sign(CA_CO_cross_product):
        return True

    return False


triangles_where_origo_included = 0

for line in list(open("problem_0102.txt")):
    points = list(map(int, line.rstrip().split(',')))
    is_contains = is_contains_origo(points)
    if is_contains:
        triangles_where_origo_included += 1

print(triangles_where_origo_included)  # 228
