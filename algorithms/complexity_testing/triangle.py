def triangle_task(
    d=None,
    dot_coords=None,
) -> int:
    """
    Check position of X relatively to triangle
    :param d: triangle leg length
    :param dot_coords: coordinates of point x
    :return: flag
    """

    if d is None:
        d = int(input())
        dot_coords = list(map(int, input().split(" ")))

    if (0 <= dot_coords[0] <= d) and (0 <= dot_coords[1] <= d):
        if sum(dot_coords) <= d:
            return 0

    dist_a = abs(dot_coords[0]) + abs(dot_coords[1])
    dist_b = abs(dot_coords[0] - d) + abs(dot_coords[1])
    dist_c = abs(dot_coords[0]) + abs(dot_coords[1] - d)

    min_dist_vertex = [dist_a, dist_b, dist_c].index(min(dist_a, dist_b, dist_c))

    return min_dist_vertex + 1


if __name__ == "__main__":
    result = triangle_task()
    print(result)
