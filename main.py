import random

def word_game():
    words = ["python", "dastur", "kompyuter", "internet", "telefon", "kitob"]
    
    secret_word = random.choice(words)
    guessed = ["_"] * len(secret_word)
    attempts = 6
    used_letters = []

    print("🎮 So‘zni topish o‘yini boshlandi!")

    while attempts > 0 and "_" in guessed:
        print("So‘z:", " ".join(guessed))
        print("Ishlatilgan harflar:", used_letters)
        print("Qolgan urinish:", attempts)

        letter = input("Harf kiriting: ").lower()

        if letter in used_letters:
            print("Bu harfni allaqachon ishlatgansiz!")
            continue

        used_letters.append(letter)

        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    guessed[i] = letter
            print("To‘g‘ri!")
        else:
            attempts -= 1
            print("Xato!")

    if "_" not in guessed:
        print("Tabriklayman! So‘zni topdingiz:", secret_word)
    else:
        print("Yutqazdingiz. So‘z:", secret_word)


word_game()
