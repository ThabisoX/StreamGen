introduction = print("Welcome to StreamGen!")

name = input('what is your name? ')
age = input('How old are you? ')
print(f'Hello {name}, Im happy to help! ')

print(f'{name} how are you feeling today' )
moods = ['Happy', 'Sad', "Bored", 'Energetic', 'Numb', "Angry", 'Great',
        "fantastic", 'Okay', "Alright", "Bad", "Not Good", "Tired", "Sleepy", 'Down'
        "Low", "Stressed", "Anxious", 'Calm', 'Relaxed', "Excited", "hyped", 
        "frustrated", "Curious", "Romantic", "Nostalgic","grumpy"
        ]
enter_mood = input(f'What is your mood? ')
process_input = enter_mood.title()
for mood in moods:
    if mood == enter_mood :
        print("what genre do you feel like Watching? ")

genres = ['Action', "Adventure", "Animation", "Biography", "Comedy", "Crime",
        "Documentary", "Drama", "Epic",  "Family", "fantasy",
        "Historical", "Horror",  'Kids', "Martial Arts"
        "Melodrama", "Musical", "Mystery",  'Philosophical',
        'Political', "Post Apocalyptic", 'Psychological', 'Romance', "Satire", 
        'Science Fiction', "Sports", "Spy", 'Super Hero', 'Super Natural', "Surreal", "Survival"
        "Thriller", "Tragedy", "War", 'Western']
print(genres)
enter_genre = input('What genre do you want to watch? ')
process_input_2 = enter_genre.title()
for genre in genres:
    if  genre == enter_genre :
        print('Which one do you prefer')

print('1. Movie')
print('2. Series')
print("3. Documentary")

user_choice = input("Enter number over here: ")
user_choice_number = int(user_choice)

if user_choice_number == 1:
    print('How much time do you want to watch')
elif user_choice_number == 2:
    print('How much time do you want to watch') 
elif user_choice_number == 3:
    print('How much time do you want to watch') 
else:
    print('Not an option please try again')

time = input("Time in minute: ")

profile_map = {("Happy", "Action"): "Happy trigger", ("Happy", "Adventure"): "Joyful Explorer", ("Happy", "Animation"): "Magic Wander", ("Happy", "Biography"): "Happy Listener", ("Happy", "Comedy"): "LOL", ("Happy", "Crime"): "Smiley Sleuth", ("Happy", "Documentary"): "Sunny Reels", ("Happy", "Drama"): "Golden Echoes",("Happy", "Epic"): "Joybound Legend", ("Happy", "Family"): "Heart & Harmony",("Happy", "Fantasy"): "WhimsyRealm", ("Happy", "Historical"): "Timeless Smiles",("Happy", "Horror"): "Giggles In The Dark!", ("Happy", "Kids"): "Giggle galaxy", ("Happy", "Martial Arts"): "Joyful Fury", ("Happy", "Melodrama"): "Tears of joy", ("Happy", "Musical"): "Melody Of Smiles", ("Happy", "Mystery"): "The Cheerful Clue", ("Happy", "Philosophical"): "Joyful Reflections", ("Happy", "Political"): "Optimistic Agenda",("Happy", "Post Apocalyptic"): "Sunshine after Ashes", ("Happy", "Psychological"): "Mindful Joy", ("Happy", "Romance"): "Heartful Harmony", ("Happy", "Sattire"): "Smiles & Sarcasm", ("Happy", "Science fiction"): "Stellar smiles", ("Happy", "Sports"): "Victory Vibes", ("Happy", "Spy"): "Secret Smiles", ("Happy", "Super Hero"): "Radiant Hero", ("Happy", "Super Natural"): "Magical bliss", ("Happy", "Surreal"): "Dreamlit Delight", ("Happy", "Survival"): "Survival's Smile", ("Happy", "Thriller"): "Thrills and Chills", ("Happy", "Tragedy"): "Tear Of Hope", ("Happy", "War"): "Victory In Peace", ("Happy", "Western"): "Sunny Trails", }