print('-' * 65)
print ('Morbid Predictions Program : ')
print()
print("Description: This program asks you for you current age and tells you the year that you will die (on average).")

age = input('What is your age today? ')
age = int(age)

print('...thinking...')
print('...thinking...')
print('...thinking...')

year = (2018 - age) + 79
year = str(year)
year = input('You will die in the year ' + year)

print(year)
print('-' * 65)
print()