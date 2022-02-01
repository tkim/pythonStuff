# old code
# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# for index, name in enumerate(names):
#     hero = heroes[index]
#     print(f'{name} is actually {hero}')

# new code
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is acutally {hero} from {universe}')