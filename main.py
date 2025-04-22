introduction = print("Welcome to StreamGen!")

name = input('what is your name? ')
age = input('How old are you? ')
print(f'Hello {name}, Im happy to help! ')

print(f'{name} how are you feeling today' )
moods = ['happy', 'Sad', "bored", 'enegetic', 'numb', "angry"]
enter_mood = input(f'What is your mood? ')
for mood in moods:
    if mood == enter_mood :
        print("what genre do you feel like Watching? ")

genres = ['']

