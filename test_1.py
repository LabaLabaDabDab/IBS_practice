def duplicate_nums(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    duplicates = []
    for num, count in num_counts.items():
        if count == 2:
            duplicates.append(num)

    if duplicates:
        return sorted(duplicates)
    else:
        return None

print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Напишите функцию, которая будет принимать список nums, содержащий числа в диапазоне от 1 до 100, и возвращать отсортированный список чисел, которые в списке nums встречались дважды.
 
Примеры:
 
duplicate_nums([1, 2, 3, 4, 3, 5, 6])
➞ [3]
 
duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54])
➞ [72, 81, 99]
 
duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
➞ None
 
Примечания:
— никакое число не будет встречаться в nums трижды и более раз,
— если никакое число в nums не встречалось дважды, функция должна вернуть None.

"""