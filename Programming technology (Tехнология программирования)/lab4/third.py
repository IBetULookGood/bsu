import random as r

def roll_dice():
    """Функция для броска двух шестигранных кубиков """
    die1= r.randint(1,6)
    die2 = r.randint(1, 6)
    return die1, die2

"""Главная фукция для игры в кости"""
print("Игра в кости")
play_again = true

while play_again:
    input("Нажмите Enter, чтобы бросить кости...")
    die1, die2 = roll_dice()
    total = die1 + die2
    print(f"Первая кость: {die1}, Вторая кость: {die2}, Общая сумма: {total}")
    play_again = input("Хотите сыграть снова? (Д/н)").lower() == 'Д'