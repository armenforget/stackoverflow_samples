s = '1 2 3 4 5 6 7 8 9 10'

delimiter = ' '
n = 3

numbers = s.split(delimiter)
group_indices = range(0, len(numbers), n)
rows = [delimiter.join(numbers[i:i+n]) for i in group_indices]
print(rows)

text_block = '\n'.join(rows)
print(text_block)
