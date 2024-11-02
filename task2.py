# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator = ','):
    # Преобразуем строки в множества, разделяя участника по указанным разделителям
    first_group_arr = set(first_group.split(separator))
    second_group_arr = set(second_group.split(separator))

    # Список общих участников
    common_el = first_group_arr.intersection(second_group_arr)

    # Возвращаем отсортированный список общих участников
    return sorted(common_el)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))# TODO Провеьте работу функции с разделителем отличным от запятой
