import os
import time
import random
from rich import print as rp

COUNT_LIVES = 3
PLAYER_LEVEL = 1
PLAYER_NAME = None
PLAYER_SCORE = 0

STATUS_GAME = True

name_list = [
            "Алекс", "Юрий", "Стив", "Гоша", "Витя", "Робик", "Бобик", 
            "Гриша", "Дмитрий", "Пупсик", "Кира", "Дуда", "Привод",
            "Назар", "Алекса", "Сири", "Алиса", "Герой", "Защитник",
            "Максим", "Гриша", "Асус", "Стерлинг", "Датик", "Даня",
            "Робот", "Ботик", "Декарь", "Ахилес", "Гелей", "Враг"
            ]
BOT_NAME = None
ENEMY_LEVEL = 0
ENEMY_LIVES = 0

def default_settings():
    global name_list, BOT_NAME, ENEMY_LEVEL, ENEMY_LIVES, STATUS_GAME, PLAYER_SCORE, PLAYER_LEVEL, COUNT_LIVES

    BOT_NAME = random.choice(name_list)
    ENEMY_LEVEL = 0
    ENEMY_LEVEL += 1
    STATUS_GAME = True
    ENEMY_LIVES = ENEMY_LEVEL + random.randint(0, ENEMY_LEVEL)

    COUNT_LIVES = 3
    PLAYER_LEVEL = 1
    PLAYER_SCORE = 0

def game_over():
    global STATUS_GAME
    STATUS_GAME = False

def minus_player_lives():
    global COUNT_LIVES
    COUNT_LIVES -= 1

def minus_enemy_lives():
    global ENEMY_LIVES
    ENEMY_LIVES -= 1

def action_after_kill():
    global PLAYER_SCORE, PLAYER_LEVEL, COUNT_LIVES
    PLAYER_SCORE += 5
    PLAYER_LEVEL += 1
    COUNT_LIVES = COUNT_LIVES + random.randint(0, PLAYER_LEVEL) + 1

def generate_enemy():
    global name_list, BOT_NAME, ENEMY_LEVEL, ENEMY_LIVES
    
    BOT_NAME = random.choice(name_list)
    ENEMY_LEVEL += 1
    ENEMY_LIVES = ENEMY_LEVEL + random.randint(0, ENEMY_LEVEL)

def get_name():
    global PLAYER_NAME
    rp(f"[orange3]{'-'*17}[/]\nВведите своё имя:\n[orange3]{'-'*17}[/]")
    while True:
        user_name = input("- ")

        if user_name in ["ㅤ", " ", None, ""]:
            PLAYER_NAME = f"Player{random.randint(100, 10000)}"
            return PLAYER_NAME

        if user_name.isdigit() == False and user_name not in [[], "", (), " ", "ㅤ"]:
            PLAYER_NAME = user_name
            return user_name

        os.system('cls||clear')
        rp(f"[orange3]{'-'*37}[/]\nИмя не может состоять только из цифр:\n[orange3]{'-'*37}[/]")