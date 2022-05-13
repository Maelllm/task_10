text_1 = 'aoeuiy'
text_2 = input('Enter your text ')
check = all([i in text_1 for i in text_2])
print(check)

list_of_numbers = input('Enter list of numbers ')
check_2 = all([i % (i ** 0.5) == 0 for i in list_of_numbers])  # Check if all numbers in list are squares

check_3 = all([True, 'helicopter', 5, 3, 4, 'U', 'False'])  # Hmm, why did result return True if there is False there...

any_1 = any('False,False,False')
any_2 = any([0, 0, 0, 0, 0])
any_3 = any([0, 0, '0', 0, 0, 0, 0, 0])

filter_1 = list(filter(str.isdigit, ['Numbers', '3', '4', 'Ome']))
filter_2 = list(filter(lambda x: x % 3 == 0, [6, 9, 5, 4, 21, 356]))
filter_3 = list(filter(None, [(), {}, 5, True, 0, False, 'p', []]))
