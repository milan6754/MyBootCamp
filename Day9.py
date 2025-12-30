#====================Encryption And Decryption=============================
'''import string
import random

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)
#print(f"chars:{chars}")
#print(f"key: {key}")

#Encryption

plain_text = input("Enter the message to Encrypt: ")
Encrypted_text=""

for letter in plain_text:
    index = chars.index(letter)

    Encrypted_text+=key[index]

print(f"Origin Message: {plain_text}")
print(f"Encrypted Message: {Encrypted_text}")

Encrypted_text = input("Enter the message to Encrypt: ")
plain_text=""

for letter in Encrypted_text:
    index = key.index(letter)

    Encrypted_text+=chars[index]

print(f"Origin Message: {Encrypted_text}")

print(f"Encrypted Message: {plain_text}")'''



#====================Hangman in python==========================

import random

words = (
    "python", "variable", "function", "loop", "string",
    "integer", "boolean", "list", "tuple", "dictionary",
    "set", "array", "index", "slice", "condition",
    "syntax", "compile", "execute", "debug", "error",
    "object", "class", "method", "attribute", "module",
    "package", "import", "return", "break", "continue",
    "input", "output", "random", "range", "while",
    "for", "elif", "else", "print", "length",
    "append", "remove", "insert", "pop", "sort",
    "reverse", "count", "find", "replace"
)

hangman_art = {
    0:("        ",
       "        ",
       "        ",),
    1:("   O   ",
       "       ",
       "       ",),
    2:("   O   ",
       "   |   ",
       "       ",),
    3:("   O   ",
       "  /|   ",
       "       ",),
    4:("   O   ",
       "  /|\\ ",
       "       ",),
    5:("   O   ",
       "  /|\\ ",
       "  /    ",),
    6:("   O    ",
       "  /|\\  ",
       "  / \\  ",)
}

def display_man(wrong_guesses):
    print("******************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************************")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(answer)

def main():
    answer = random.choice(words)
    hint = ["_"] *len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter the letter: ").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess  in guessed_letter:
            print(f"{guess} is already guessed.")
            continue
        guessed_letter.add(guess)

        if guess in answer:
            for  i in range(len(answer)):
                if answer[i] ==guess:
                    hint[i] = guess 

        else:
            wrong_guesses+=1
        
        if "_" not in  hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win ")

            is_running=False
        elif  wrong_guesses >=len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose")
            is_running=False


if __name__ == "__main__":
    main()

