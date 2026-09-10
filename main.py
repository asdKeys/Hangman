import random

word = "e"
letter1 = "e"
letter2 = "e"
letter3 = "e"
letter4 = "e"
letter5 = "e"
letter6 = "e"
guessed_letter= "e"
lives = 10
alt_letter1 = "_"
alt_letter2 = "_"
alt_letter3 = "_"
alt_letter4 = "_"
alt_letter5 = "_"
alt_letter6 = "_"
finish = 1
score = 0

def select_word():
    global word
    words = ["animal", "circle", "doctor", "energy", "garden", "island", "jungle", "office", "defend", "police", "python"]
    word = random.choice(words)
    
def split_word():
    global word
    global letter1
    global letter2
    global letter3
    global letter4
    global letter5
    global letter6
    if word == "animal":
        letter1 = "a"
        letter2 = "n"
        letter3 = "i"
        letter4 = "m"
        letter5 = "a"
        letter6 = "l"
    if word == "circle":
        letter1 = "c"
        letter2 = "i"
        letter3 = "r"
        letter4 = "c"
        letter5 = "l"
        letter6 = "e"
    if word == "doctor":
        letter1 = "d"
        letter2 = "o"
        letter3 = "c"
        letter4 = "t"
        letter5 = "o"
        letter6 = "r"
    if word == "energy":
        letter1 = "e"
        letter2 = "n"
        letter3 = "e"
        letter4 = "r"
        letter5 = "g"
        letter6 = "y"
    if word == "garden":
        letter1 = "g"
        letter2 = "a"
        letter3 = "r"
        letter4 = "d"
        letter5 = "e"
        letter6 = "n"
    if word == "island":
        letter1 = "i"
        letter2 = "s"
        letter3 = "l"
        letter4 = "a"
        letter5 = "n"
        letter6 = "d"
    if word == "jungle":
        letter1 = "j"
        letter2 = "u"
        letter3 = "n"
        letter4 = "g"
        letter5 = "l"
        letter6 = "e"
    if word == "office":
        letter1 = "o"
        letter2 = "f"
        letter3 = "f"
        letter4 = "i"
        letter5 = "c"
        letter6 = "e"
    if word == "defend":
        letter1 = "d"
        letter2 = "e"
        letter3 = "f"
        letter4 = "e"
        letter5 = "n"
        letter6 = "d"
    if word == "police":
        letter1 = "p"
        letter2 = "o"
        letter3 = "l"
        letter4 = "i"
        letter5 = "c"
        letter6 = "e"
    if word == "python":
        letter1 = "p"
        letter2 = "y"
        letter3 = "t"
        letter4 = "h"
        letter5 = "o"
        letter6 = "n"
        
def text():
    global lives
    global score
    print("Score: ", score)
    print("Lives: ", lives)
    print(alt_letter1, alt_letter2, alt_letter3, alt_letter4, alt_letter5, alt_letter6)
    
def enter_letter():
    global guessed_letter
    global letter1
    global letter2
    global letter3
    global letter4
    global letter5
    global letter6
    global lives
    global alt_letter1
    global alt_letter2
    global alt_letter3
    global alt_letter4
    global alt_letter5
    global alt_letter6
    global score
    guessed_letter = input("Guess Letter Here: ")
    if guessed_letter == letter1:   
        alt_letter1 = letter1
        score = score + 100
    if guessed_letter == letter2:
        alt_letter2 = letter2
        score = score + 85
    if guessed_letter == letter3:
        alt_letter3 = letter3
        score = score + 25
    if guessed_letter == letter4:
        alt_letter4 = letter4
        score = score + 105
    if guessed_letter == letter5:
        alt_letter5 = letter5
        score = score + 90
    if guessed_letter == letter6:
        alt_letter6 = letter6
        score = score + 75
    if guessed_letter not in [letter1, letter2, letter3, letter4, letter5, letter6]:
        print("This Letter Is Not In The Word")
        lives = lives - 1
        
def game_loop():
    global lives
    global finish
    while finish == 1 and lives > 0:
        text()
        enter_letter()
        die()
        finish_word()
    
def die():
    global lives
    if lives < 1:
        print("")
        print("YOU DIED")
        print("")
        
def main_loop():
    global lives
    global finish
    print("Guess The Word. You Have 10 Lives")
    while lives > 0:
        reset()
        select_word()
        split_word()
        game_loop()
        text()
    
def finish_word():
    global alt_letter1
    global alt_letter2
    global alt_letter3
    global alt_letter4
    global alt_letter5
    global alt_letter6
    global finish
    global lives
    if alt_letter1 != "_" and alt_letter2 != "_" and alt_letter3 != "_" and alt_letter4 != "_" and alt_letter5 != "_" and alt_letter6 != "_":
        finish = 2
        print("You Completed This Word")
        lives = lives + 2
        
def reset():
    global guessed_letter
    global finish
    global word
    global letter1
    global letter2
    global letter3
    global letter4
    global letter5
    global letter6
    global alt_letter1
    global alt_letter2
    global alt_letter3
    global alt_letter4
    global alt_letter5
    global alt_letter6
    guessed_letter = "e"
    finish = 1
    word = "e"
    letter1 = "e"
    letter2 = "e"
    letter3 = "e"
    letter4 = "e"
    letter5 = "e"
    letter6 = "e"
    alt_letter1 = "_"
    alt_letter2 = "_"
    alt_letter3 = "_"
    alt_letter4 = "_"
    alt_letter5 = "_"
    alt_letter6 = "_"
    
    
main_loop()

