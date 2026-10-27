def find_largest(numbers):
  if not numbers:
    return None

  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num

  return largest
num = find_largest([-10, -5, -2, -18])
print(num)

  
































"""def count_even(numbers):
 for 1 n in numbers:
    if n % 2 == 0:
        return sum() 
num = count_even( [1, 2, 3, 4, 6])  
print(num) """ 



"""