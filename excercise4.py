def count_even(numbers):
    count = 0  # Initialize a counter
    for n in numbers:  
        if n % 2 == 0:  
            count += 1  
    return count 

num = count_even([1, 2, 3, 4, 6])   
print(num)
