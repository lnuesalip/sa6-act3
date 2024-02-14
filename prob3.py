def max_lst(func, numbers):
    i = 0
    current_max = numbers[0]
    for i in range(len(numbers)):
        current_max = func(current_max, numbers[i])

    return current_max


numbers = [2, 5, 1, 2, 3, 4, 16, 9, 10]
greater = lambda a, b: a if a > b else b 
print(max_lst(greater, numbers))


    