import random

# Слова для игры
WORDS = ["питон", "программист", "виселица", "компьютер", "алгоритм", "функция", "переменная"]

# Этапы виселицы: 0 ошибок -> 6 ошибок (повешен)
STAGES = [
    # 0 ошибок
    """
       -----
       |   |
           |
           |
           |
           |
           |
    =========
    """,
    # 1 ошибка — голова
    """
       -----
       |   |
       O   |
           |
           |
           |
           |
    =========
    """,
    # 2 ошибки — туловище
    """
       -----
       |   |
       O   |
       |   |
           |
           |
           |
    =========
    """,
    # 3 ошибки — левая рука
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
           |
    =========
    """,
    # 4 ошибки — правая рука
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
           |
    =========
    """,
    # 5 ошибок — левая нога
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
           |
    =========
    """,
    # 6 ошибок — правая нога — ПОВЕШЕН
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
           |
    =========
    """,
]

# Финальная сцена — смерть (крестики на глазах + язык)
DEAD = """
       -----
       |   |
       X   |
      /|\\  |
      / \\  |
           |
           |
    =========

    💀 ОН УМЕР. Ты его убил. 💀
"""


def show_word(word, guessed):
    """Показывает слово с угаданными буквами и прочерками."""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0
    max_wrong = len(STAGES) - 1  # 6

    print("🎮 ИГРА «ВИСЕЛИЦА»")
    print("Спаси человечка — угадай слово по буквам!\n")

    while True:
        print(STAGES[wrong])
        print("Слово:", show_word(word, guessed))
        print(f"Ошибок: {wrong}/{max_wrong}")
        print("Угаданные буквы:", ", ".join(sorted(guessed)) or "—")
        print()

        # Проверка победы
        if all(ch in guessed for ch in word):
            print("🎉 ТЫ ПОБЕДИЛ! Человечек спасён!")
            print(f"Слово было: {word}")
            break

        # Проверка проигрыша
        if wrong >= max_wrong:
            print(DEAD)
            print(f"Слово было: {word}")
            break

        letter = input("Введи букву: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("⚠️  Нужна одна буква (русская).\n")
            continue

        if letter in guessed:
            print("🔁 Ты уже называл эту букву.\n")
            continue

        guessed.add(letter)

        if letter in word:
            print("✅ Есть такая буква!\n")
        else:
            wrong += 1
            print(f"❌ Нет такой буквы! Ошибок: {wrong}/{max_wrong}\n")


if __name__ == "__main__":
    play()