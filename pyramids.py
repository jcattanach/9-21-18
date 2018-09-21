def pyramids(num_of_rows):
    for index in range(num_of_rows):
        print(' ' * (num_of_rows - index - 1) + '*' * (2 * index + 1))

pyramids(9)
