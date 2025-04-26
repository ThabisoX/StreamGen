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
    if mood == process_input :
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

time = int(input("Time in minute (e.g  50 = 30 minutes, 100 = 1Hr , 150 = 1hr30min: "))

if time == 50:
    pass
elif time == 100:
    pass
elif time == 150:
    pass

def get_profile_name(mood, genre):
    mood_genre_profiles = {
        "Happy": {
            "Action": "Happy Trigger",
            "Adventure": "Joyful Wanderer",
            "Animation": "Happy Pixel",
            "Biography": "Truly Happy",
            "Comedy": "HAA HAA HAA Jokes on you",
            # ...add more genres for "Happy" mood...
        },
        "Sad": {
            "Action": "Echoes of Valor",
            "Adventure": "Wanderer's Lament",
            "Animation": "Bittersweet Frames",
            "Biography": "Echoes of a life",
            "Comedy": "Tears & chuckles",
            # ...add more genres for "Sad" mood...
        },
        # ...add more moods with their genre mappings...
    }

    mood_profiles = mood_genre_profiles.get(mood, {})
    return mood_profiles.get(genre, "Unknown Profile")

# Example usage:
profile = get_profile_name(process_input, process_input_2)
print(f"Wow, your profile is: {profile}!")

