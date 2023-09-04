int1 = int(input('Enter first number: '))
int2 = int(input('Enter second number: '))
int3 = int(input('Enter third number: '))

#int2 is only a placeholder
maximum = int2

if maximum < int1:
    maximum = int1
elif maximum < int3:
    maximum = int3
else:
    maximum = int1


print(f'the maximum number is {maximum}')