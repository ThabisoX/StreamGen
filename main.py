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

def decide_profile(process_input, process_input_2 ):
    if process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
    
    elif process_input == "Sad":
        if process_input_2 == "Action":
            return "Echoes of Valor"
        elif process_input_2 == "Adventure":
            return "Wanderer's Lament"
        elif process_input_2 == "Animation":
            return "Bittersweet Frames"
        elif process_input_2 == "Biography":
            return "Echoes of a life"
        elif process_input_2 == "Comedy":
            return "Tears & chuckles"
        elif process_input_2 == "Crime":
            return "Smiley Broken Justice"
        elif process_input_2 == "Documentary":
            return "Sunny Tears In Tears"
        elif process_input_2 == "Drama":
            return "Golden Shadows of Heart"
        elif process_input_2 == "Epic":
            return "Echoes Of Glory"
        elif process_input_2 == "Family":
            return "Fractured bonds"
        elif process_input_2 == "Fantasy":
            return "Tears Of The Realm"
        elif process_input_2 == "Historical":
            return "Smiles Eras"
        elif process_input_2 == "Horror":
            return "Whispers Of the Forgotten"
        elif process_input_2 == "Kids":
            return "Lost lullabies"
        elif process_input_2 == "Martial Arts":
            return "fallen Warrior"
        elif process_input_2 == "Melodrama":
            return "Crimson Tears"
        elif process_input_2 == "Musical":
            return "Dissonant hearts"
        elif process_input_2 == "Mystery":
            return "Echoes of the Unsolved"
        elif process_input_2 == "Philosophical":
            return "Sorrowful Truths"
        elif process_input_2 == "Political":
            return "Shattered Ideals"
        elif process_input_2 == "Post Apocalyptic":
            return "Echoes Of a Dying World"
        elif process_input_2 == "Psychological":
            return "Fractured Minds"
        elif process_input_2 == "Romance":
            return "Love's Last Breath"
        elif process_input_2 == "Satire":
            return "Cynical smiles"
        elif process_input_2 == "Science Fiction":
            return "Fading Stars"
        elif process_input_2 == "Sports":
            return "Fallen Champions"
        elif process_input_2 == "Spy":
            return "Shadows O Betrayal"
        elif process_input_2 == "Superhero":
            return "Broken Capes"
        elif process_input_2 == "Super Natural":
            return "Wraiths Of The Past"
        elif process_input_2 == "Surreal":
            return "Shatterd Realms"
        elif process_input_2 == "Survival":
            return "Lonely Horizon"
        elif process_input_2 == "Thriller":
            return "The Last Breath"
        elif process_input_2 == "Tragedy":
            return "Shattered Dreams"
        elif process_input_2 == "War":
            return "Echoes of the Fallen"
        
    elif process_input == "Bored":
        if process_input_2 == "Action":
            return "Stale Fury"
        elif process_input_2 == "Adventure":
            return "Wanderer In Stillness"
        elif process_input_2 == "Animation":
            return "Frozen Frames"
        elif process_input_2 == "Biography":
            return "Tales Untold"
        elif process_input_2 == "Comedy":
            return "Yawns & Yucks"
        elif process_input_2 == "Crime":
            return "Crime Of Routine"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Energetic":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
    
    elif process_input == "Numb":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Angry":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Great":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
    elif process_input == "Happy":
        if process_input_2 == "Action":
            return "Happy Trigger"
        elif process_input_2 == "Adventure":
            return "Joyful Wanderer"
        elif process_input_2 == "Animation":
            return "Happy Pixel"
        elif process_input_2 == "Biography":
            return "Truly Happy"
        elif process_input_2 == "Comedy":
            return "HAA HAA HAA Jokes on you"
        elif process_input_2 == "Crime":
            return "Smiley Sleuth"
        elif process_input_2 == "Documentary":
            return "Sunny Reels"
        elif process_input_2 == "Drama":
            return "Golden Echoes"
        elif process_input_2 == "Epic":
            return "JoyBound Legends"
        elif process_input_2 == "Family":
            return "Heart & Harmony"
        elif process_input_2 == "Fantasy":
            return "WhimsyRealms"
        elif process_input_2 == "Historical":
            return "Timeless Smiles"
        elif process_input_2 == "Horror":
            return "Giggles in the Dark"
        elif process_input_2 == "Kids":
            return "Giggle Galaxy"
        elif process_input_2 == "Martial Arts":
            return "joyful Fury"
        elif process_input_2 == "Melodrama":
            return "Tears of joy"
        elif process_input_2 == "Musical":
            return "Melody of smiles"
        elif process_input_2 == "Mystery":
            return "The Cheerful Clue"
        elif process_input_2 == "Philosophical":
            return "Joyful Reflections"
        elif process_input_2 == "Political":
            return "Optimistic Agenda"
        elif process_input_2 == "Post Apocalyptic":
            return "Sunshine After Ashes"
        elif process_input_2 == "Psychological":
            return "Mindful Joy"
        elif process_input_2 == "Romance":
            return "HeartFelt Harmony"
        elif process_input_2 == "Satire":
            return "Smile & Sarcasm"
        elif process_input_2 == "Science Fiction":
            return "Stellar Smiles"
        elif process_input_2 == "Sports":
            return "Victory Vibes"
        elif process_input_2 == "Spy":
            return "Secret Smiles"
        elif process_input_2 == "Superhero":
            return "Radiant Hero"
        elif process_input_2 == "Super Natural":
            return "Magical Bliss"
        elif process_input_2 == "Surreal":
            return "Dreamlit Delight"
        elif process_input_2 == "Survival":
            return "Survivors Smile"
        elif process_input_2 == "Thriller":
            return "Thrills & Chills"
        elif process_input_2 == "Tragedy":
            return "Tears Of Hope"
        elif process_input_2 == "War":
            return "Sunny Trails"
        
        
        
        
        
        
        
profile = decide_profile(process_input, process_input_2)
print(f"OW wow; {profile}!")