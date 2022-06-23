import math


def school_geo_plan(
    number_of_students=None,
    coords=None,
) -> int:
    """
    Finding best school position
    :param number_of_students: number of students in school
    :param coords: coordinates of pupil's homes
    :return: 
    """
    if number_of_students is None:
        number_of_students = int(input())
        coords = list(map(int, input().split(" ")))

    if number_of_students == 0:
        return 0
    if number_of_students == 1:
        return coords[0]

    position = coords[math.ceil(number_of_students / 2) - 1]

    return position


if __name__ == "__main__":
    result = school_geo_plan()
    print(result)
