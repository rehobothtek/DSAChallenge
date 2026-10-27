def count_occurrences(numbers, target):
    occurrences = 0
    for num in numbers:
        if num == target:
            occurrences += 1
    return occurrences


cal =  count_occurrences(numbers = [2, 5, 2, 8, 2], target = 2)
print(cal)




