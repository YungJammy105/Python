def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end='\t')
        print()

    print([i * j for i in range(1, num_rows + 1) for j in range(1, num_columns + 1)])




print_operation_table(lambda x, y: x * y, int(input('row count = ')), int(input('count of columns = ')))