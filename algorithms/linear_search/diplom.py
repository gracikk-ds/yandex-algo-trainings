def diploma_time(
        amount_of_folders=None,
        diploma_amount_per_folder=None
) -> int:
    """
    Finding minimal time
    :param amount_of_folders: folders to check
    :param diploma_amount_per_folder: amount of diplomas in each folder
    :return: minimal time
    """
    if amount_of_folders is None:
        amount_of_folders = int(input())
        diploma_amount_per_folder = list(map(int, input().split()))

    diploma_amount_per_folder.sort()
    time = sum(diploma_amount_per_folder[:-1])
    return time


if __name__ == "__main__":
    result = diploma_time()
    print(result)
