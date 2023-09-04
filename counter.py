strnum = input('Please enter a number: ')

print('\n')

length, smallest, biggest = 0, 9, 0
flag = False

if strnum == '0':
    length = 1

while strnum:
    digit = int(strnum[-1])  # Get the last digit
    length += 1

    if not flag or digit < smallest:
        smallest = digit
        flag = True

    if digit > biggest:
        biggest = digit

    strnum = strnum[:-1]  # Remove the last digit

print(f'Number of digits in the given number is: {length}')
print(f'Smallest number is: {smallest}')
print(f'Highest number is: {biggest}')
