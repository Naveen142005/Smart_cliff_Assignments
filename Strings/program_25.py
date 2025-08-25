# reading input
n = int(input())
input_list = [int(input()) for i in range(n)]

# removing duplicates
input_list = list(set(input_list))
n = len(input_list)

# showing menu of operations
print("""1. Remove duplicates from the list. 
2. Calculate the sum of unique values in the list. 
3. Calculate the mean of unique values in the list. 
4. Find the largest and smallest unique values in the list. 
5. Quit the program.""")

while True:
    # taking user choice and processing
    print('Enter a choice:')
    choose = int(input())

    match choose:
        case 1:
            print('List with duplicates removed:', end=' ')
            print(input_list)

        case 2:
            print('Sum of unique values:', end=' ')
            print(sum(input_list))

        case 3:
            print('Mean of unique values:', end=' ')
            mean = sum(input_list) / n
            print(mean)

        case 4:
            print('Largest value', end=' ')
            print(max(input_list))
            print('Smallest value', end=' ')
            print(min(input_list))

        case 5:
            break

        case _:
            print('Invalid choice')
