def first_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None
num = first_duplicate([5, 5, 3])
print(num)    