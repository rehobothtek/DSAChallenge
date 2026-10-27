def move_zeros(numbers):
  non_zeros = [num for num in numbers if num != 0]
  zeros_count = len(numbers) - len(non_zeros)
  return non_zeros + [0] * zeros_count

cal = move_zeros([0, 0, 5])
print(cal)