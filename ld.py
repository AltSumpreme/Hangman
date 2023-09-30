import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel",
  "discovery", 
    "know", 
      "street", "felt",
      "thumb", "won",
      "officer", "situation",
      "judge", "brain",
      "rose", "circle",
      "party", "equal",
      "such", "population",
      "while", "desk",
      "hundred", "mood",
      "easier", "consonant",
      "darkness", "percent",
      "ill", "chapter",
      "practical", "fox",
      "chest", "piano",
      "taste", "tide",
      "feel", "increase",
      "talk", "shoe",
      "walk", "goes",
      "constantly", "soap",
      "scientist", "ought",
      "boat", "environment",
      "native", "music",
      "soft", "shake",
      "definition", "thumb",
      "white", "tide",
      "between", "till",
      "care", "sky",
      "bow", "kitchen",
      "arrangement", "stepped",
      "third", "member",
      "upon", "still",
      "key", "ruler",
      "solve", "itself",
      "made", "word",
      "farmer", "cap",
      "needed", "adult",
      "never", "social",
      "my", "dream",
      "written", "feathers",
      "usually", "chief",
      "history", "dinner",
      "early", "raise",
      "bit", "have",
      "differ", "them",
      "greatest", "region",
      "until", "stand",
      "bill", "select",
      "birthday", "end",
      "it", "individual",
      "broken", "wolf"
    ,
    "cave", "since",
    "breathe", "shout",
    "speed", "bicycle",
    "stay", "distance",
    "single", "rays",
    "alike", "very",
    "include", "clothing",
    "charge", "sort",
    "topic", "cowboy",
    "round", "thee",
    "pen", "lost",
    "fill", "help",
    "carbon", "quarter",
    "pleasure", "curve",
    "saved", "break",
    "recall", "send",
    "forth", "real",
    "hundred", "newspaper",
    "warn", "highway",
    "south", "announced",
    "into", "upper",
    "beginning", "syllable",
    "dangerous", "judge",
    "solar", "during",
    "fight", "tropical",
    "door", "string",
    "rain", "another",
    "time", "care",
    "finish", "electricity",
    "fierce", "within",
    "native", "living",
    "had", "officer",
    "chair", "date",
    "surrounded", "pie",
    "pale", "surrounded",
    "military", "never",
    "feathers", "ten",
    "writer", "facing",
    "husband", "cave",
    "sweet", "medicine",
    "on", "fear",
    "flies", "determine",
    "instant", "donkey",
    "adventure", "women",
    "game", "extra",
    "drive", "discuss",
    "arrange", "hay",
    "molecular", "stems",
    "trick", "product"
 ,
  "better", "bear",
  "without", "stranger",
  "coming", "certainly",
  "voice", "week",
  "melted", "compass",
  "decide", "pour",
  "eager", "leave",
  "must", "round",
  "kind", "finger",
  "spirit", "club",
  "quickly", "able",
  "become", "image",
  "just", "born",
  "remember", "hardly",
  "found", "front",
  "one", "put",
  "rhythm", "gasoline",
  "vast", "we",
  "shut", "soft",
  "hard", "select",
  "evidence", "object",
  "sell", "railroad",
  "stomach", "which",
  "structure", "related",
  "sitting", "people",
  "over", "contrast",
  "read", "store",
  "contain", "keep",
  "offer", "dirty",
  "gave", "visitor",
  "smooth", "grandmother",
  "mental", "volume",
  "close", "body",
  "pleasure", "here",
  "compare", "game",
  "remarkable", "bound",
  "month", "ever",
  "picture", "army",
  "deep", "pilot",
  "standard", "including",
  "dull", "done",
  "ball", "want",
  "also", "parts",
  "easily", "official",
  "thin", "cross",
  "joy", "careful"
]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
display = []
for _ in range(word_length):
    display += "_"
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:  
      print(f"You guessed {guess}, that's not in the word.") 
      lives -= 1
      if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(stages[lives])
print(f"The word is {chosen_word}")
