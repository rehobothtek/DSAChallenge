
def has_duplicates(numbers):
  seen = set()
  for num in numbers:
    if num in seen:
      return True
    seen.add(num)
  data = False
  return False

cal = has_duplicates([])
print(cal)  
