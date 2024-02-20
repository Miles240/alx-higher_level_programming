# def greet(language: str, *peolpe: str):
#     if language == 'it':
#         greeting = 'Ciao'
#     else:
#         greeting = 'Hello'

#     for person in peolpe:
#         print(f'{greeting} {person}')

# greet('en', 'miles')


# def add_nums(*num, tet):
#     num = [number for number in num]
#     print(sum(num), tet)


# add_nums(1, 2, 3, 4, 5, tet="is the sum")

def kwargs(**user):
    print(user)
    for name in user.items():
        print(name)

kwargs(user1= 'miles', user2= 'pius')