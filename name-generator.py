import random

first = ['Andrew', 'Alice', 'Emily', 'Webster']

second = ['Drastically', 'Unforgettably', 'Painfully', 'Absolutely']

third = ['Daring', 'Cunning', 'Optimistic', 'Strong', 'Barbaric']

connect = ' the '

full_names = []

for name in first:
    the_name = name + connect + random.choice(second) + ' ' + random.choice(third)
    full_names.append(the_name)


final_list = ', '.join(full_names)


print(final_list)
