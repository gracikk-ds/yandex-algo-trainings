from typing import Union, Any


def interactor_verdict(
    task_code=None, interactor_result=None, checker_result=None
) -> Union[Union[str, int], Any]:
    """
    1. Interactor task
    :param task_code: код завершения задачи
    :param interactor_result: вердикт интерактора
    :param checker_result: Вердикт чекера
    :return: итоговый вердикт
    """

    if task_code is None:
        print("Please, input task code:")
        task_code = int(input())
    else:
        print(f"task_code value: {task_code}")

    if interactor_result is None:
        print("Please, input interactor result:")
        interactor_result = int(input())
    else:
        print(f"interactor_result value: {interactor_result}")

    if checker_result is None:
        print("Please, input checker result:")
        checker_result = int(input())
    else:
        print(f"checker_result value: {checker_result}")

    if (127 < task_code) | (-127 > task_code):
        print("TaskCode Error")
        return "Input Error"
    if (7 < interactor_result) | (0 > interactor_result):
        print("InteractorResult Error")
        return "Input Error"

    if (7 < checker_result) | (0 > checker_result):
        print("CheckerResult Error")
        return "Input Error"

    if interactor_result == 0:
        if task_code != 0:
            print(3)
            return 3
        else:
            print(checker_result)
            return checker_result

    elif interactor_result == 1:
        print(checker_result)
        return checker_result

    elif interactor_result == 4:
        if task_code != 0:
            print(3)
            return 3
        else:
            print(4)
            return 4

    elif interactor_result == 6:
        print(0)
        return 0

    elif interactor_result == 7:
        print(1)
        return 1

    else:
        return interactor_result


if __name__ == "__main__":
    result = interactor_verdict()
    print(f"interactor_result: {result}")
