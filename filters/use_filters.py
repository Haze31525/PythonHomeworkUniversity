import random


def apply_random_function(objects_list, functions_list):
    """
    Применяет случайную функцию из списка functions_list к каждому объекту из списка objects_list.
    :param objects_list: список объектов
    :param functions_list: список функций
    :return: список объектов после применения функций
    """

    result_list = []
    for obj in objects_list:
        # выбираем случайную функцию из списка
        random_func = random.choice(functions_list)
        # применяем выбранную функцию к объекту
        result = random_func(obj)
        result_list.append(result)
    return result_list
