numbers = []
for i in range(10, 71):
    numbers.append(i)
even_numbers = [num for num in numbers if num % 2 == 0]
powers_of_2 = [num for num in numbers if (num & (num - 1)) == 0]
print("Even numbers:", even_numbers)
print("Powers of 2:", powers_of_2)
