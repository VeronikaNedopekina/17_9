def sort_seq(sequence_numbers):
    for i in range(1, len(sequence_numbers)):
        x = sequence_numbers[i]
        idx = i
        while idx > 0 and sequence_numbers[idx-1] > x:
            sequence_numbers[idx] = sequence_numbers[idx-1]
            idx -= 1
        sequence_numbers[idx] = x
    return sequence_numbers


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def get_list():
    try:
        str = input('Enter a sequence of space-separated integer numbers:\t')
        if " " not in str:
            print("\nThere aren't any spaces between the numbers, follow the rule")
            return False
        sequence_numbers = str.split()
        sequence_numbers = [int(item) for item in sequence_numbers]
    except ValueError:
        print('ERROR Enter a sequence of space-separated integer numbers')
        return False
    sequence_numbers = sort_seq(sequence_numbers)
    return sequence_numbers


def get_number(sequence_numbers):
    try:
        number = int(input('Enter an integer number:\t'))
    except ValueError:
        print('ERROR Please enter correct number')
        return False
    if not sequence_numbers[0] < number < sequence_numbers[-1]:
        print('Please enter the number within the entered sequence of numbers')
        return False
    return number


while True:
    sequence_numbers = get_list()
    if sequence_numbers:
        break

while True:
    number = get_number(sequence_numbers)
    if type(number) == int:
        break

print(f'Sorted sequence of numbers: {sequence_numbers}')
position = binary_search(sequence_numbers, number, 0, len(sequence_numbers))
a = min(sequence_numbers, key=lambda x: (abs(x - number), x))
ind = sequence_numbers.index(a)
if not position:
    print(f'Position of smaller number is {ind}, position of bigger (same) number is {ind + 1}')
else:
    print(f'Position of smaller number is {ind - 1}, position of bigger (same) number is {ind + 1}')
