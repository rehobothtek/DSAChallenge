def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
cal = list_sum([2, 4, 6, 8])
print(cal)