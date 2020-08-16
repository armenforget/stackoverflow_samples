def get_right_number(numbers, i):
    if i >= len(numbers) - 1:
        right = -99
    else:
        right = numbers[i + 1]
        if right == -99:
            right = get_right_number(numbers, i+1)
    return right


def clean_missing_data(numbers):
    print(f'Input: {numbers}')

    if all(x == -99 for x in numbers):
        print('All values in list are invalid. Could not compute.')
        return

    clean_numbers = []

    for i in range(len(numbers)):
        if numbers[i] != -99:
            clean_numbers.append(numbers[i])
        else:
            valid_count = 0

            if i == 0:
                left = 0
            else:
                left = clean_numbers[i - 1]
                valid_count += 1

            right = get_right_number(numbers, i)
            if right == -99:
                right = 0
            else:
                valid_count += 1

            average = (left + right) / valid_count
            clean_numbers.append(average)

    print(f'Output: {clean_numbers}\n')
    return clean_numbers


clean_missing_data([1, 2, 3, 4, 5])
clean_missing_data([1, 2, 3, -99, 5])
clean_missing_data([-99, 2, 3, 4, 5])
clean_missing_data([-99, -99, 3, 4, 5])
clean_missing_data([1, 2, 3, 4, -99])
clean_missing_data([1, 2, 3, -99, -99])
clean_missing_data([1, -99, -99, -99, 5])
clean_missing_data([-99, -99, -99, -99, -99])
