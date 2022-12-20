import os, sys, time
import settings, models
import game_exceptions as gex
from rich import print as rp

def clear():
    os.system('cls||clear')

def exit_game():
    sys.exit()

def leaders():
    check = False
    count_underlines = 17
    while check == False:
        try:
            rs = []
            with open("scores.txt", "r") as file:
                for line in file:
                    rs.append(line)

            rp(f"""[orange3]{"-"*count_underlines*2}[/]""")
            rp(f"""{"".join(rs)}""")
            rp(f"""[orange3]{"-"*count_underlines*2}[/]\n| 1 - Выйти в меню\n[orange3]{"-"*count_underlines*2}[/]""")
            res = int(input("- "))
            
            if res == 1:
                check = True
                clear()
                game()
            else:
                clear()
        except:
            clear()

def rules():
    check = False
    count_underlines = 17
    while check == False:
        try:
            rp(
f"""[orange3][bold]Продвинутые камень ножницы бумага[/][/] - игра, в которой вам необходимо выбрать своего персонажа \
и испытать удачу против бота. Всего на выбор вам дается 3 варианта: [orange3]Чародей(1), Воин(2), Разбойник(3)[/]. \
Правила точно такие же как и у оригинальной игры, Чародей побеждает воина. Воин побеждает разбойника. Разбойник побеждает колдуна. \
У каждого врага есть определенное количество жизней, уровень и жизни бота растут после каждой вашей победы. \
У вашего персонажа так же есть свой уровень, очки и жизни. После каждой победы над противником вы будите получать \
+5 поинтов, +1 уровень и + рандомное количество жизней в зависимости от вашего уровня. За каждый нанесенный урон по противнику \
количество важих баллов увеличивается на 1. Количество противников бесконечно, и с каждым побежденным раундом сложность растет. \n"""
                )

            rp(f"""[orange3]{"-"*count_underlines*2}[/]\n| 1 - Выйти в меню\n[orange3]{"-"*count_underlines*2}[/]\n{' '*4}""")
            res = int(input("- "))
            
            if res == 1:
                check = True
                clear()
                game()
            else:
                clear()
        except:
            clear()

def game():

    clear()
    settings.generate_enemy()

    player = models.Player(settings.PLAYER_NAME, settings.COUNT_LIVES, settings.PLAYER_SCORE, settings.PLAYER_LEVEL, 0)
    enemy = models.Enemy(settings.ENEMY_LEVEL, settings.BOT_NAME)

    name = settings.PLAYER_NAME
    count_underlines = '-'*(27+len(name))
    
    action = False
    result_action = None
    
    while action == False:
        try:
            rp(f"""[orange3]{count_underlines}[/]\n{' '*3}Добро пожаловать, [green][bold]{name}[/][/]!\n[orange3]{count_underlines}[/] \n| 1 - Начать \n| 2 - Рейтинг \n| 3 - Правила\n| 4 - Выход\n[orange3]{count_underlines}[/]""")
            player_action = int(input("- "))

            if player_action not in [1, 2, 3, 4]:
                clear()

            if player_action == 1:
                result_action = "game"
                action = True

            if player_action == 2:
                result_action = "top"
                action = True

            if player_action == 3:
                result_action = "rules"
                action = True

            if player_action == 4:
                action = True
                exit_game()
            
        except:
            clear()

    if result_action == "game":
        
        clear()
        settings.default_settings()
        
        count_underlines = 17
        count_space_for_bot = ' '*(len(settings.BOT_NAME)-3 if len(settings.BOT_NAME) > 5 else len(settings.BOT_NAME))
        round_game = 0

        stop_limit = True
        while stop_limit:
            player = models.Player(settings.PLAYER_NAME, settings.COUNT_LIVES, settings.PLAYER_SCORE, settings.PLAYER_LEVEL, 0)
            enemy = models.Enemy(settings.ENEMY_LEVEL, settings.BOT_NAME)

            text_game = None
            type_game = None

            round_game += 1
            if round_game % 2 == 0:
                text_game = "защищаетесь"
                type_game = 1
            else:
                text_game = "атакуете"
                type_game = 2

            rp(f"""[orange3]{"-"*count_underlines*2}[/]\n{' '*12}Раунд {round_game}!\n[orange3]{"-"*count_underlines*2}[/]\n\n""")    
            rp(
                f"""[orange3]{"-"*(count_underlines)*2}[/]\n{' '*3}{name}:{' '*3}{count_space_for_bot}{enemy.name}:\n[orange3]{"-"*(count_underlines)*2}[/]\
                \n| Прогресс: {player.level}   | Прогресс: {enemy.level}    |\
                \n| Здоровье: {player.lives}   | Здоровье: {enemy.lives}    |\
                \n| Тв. очки: {player.score}   |                |\
                \n[orange3]{"-"*(count_underlines)*2}[/]\n
                """
                )
            check = False
            player_class = None

            if settings.STATUS_GAME == False:
                check = True
                player_class = 5

            while check == False:

                rp(f"""[orange3]{"-"*count_underlines*2}[/]\n{' '*10}Вы [bold]{text_game}[/]!\n{' '*3}Выберите класс своего война:\n[orange3]{"-"*count_underlines*2}[/]\n| 1 - Чародей \n| 2 - Воин \n| 3 - Разбойник\n| 4 - Выход\n[orange3]{"-"*count_underlines*2}[/]""")
                try:
                    player_class = int(input("- "))
                    if player_class == 4:
                        stop_limit = False
                        check = True
                        settings.default_settings()
                        game()

                    elif player_class in [1, 2, 3]:
                        clear()
                        check = True
                    else:
                        clear()
                except:
                    clear()
                
            clear()
            
            result_fight = None
            who_win = None

            if type_game == 1:
                bot_choice = enemy.select_attack()
                result_fight = player.attack(player_class, bot_choice)

                if result_fight == 0:
                    who_win = "Ничья"
                elif result_fight == int("-1"):
                    who_win = player.name
                else:
                    who_win = f"Бот {enemy.name}"

            elif type_game == 2:
                bot_choice = enemy.select_attack()
                result_fight = player.defence(bot_choice, player_class)

                if result_fight == 0:
                    who_win = "Ничья"
                elif result_fight == int("-1"):
                    who_win = f"Бот {enemy.name}"
                else:
                    who_win = player.name

            clear()

            if player_class not in [4, 5]:
                player_text = "None"
                enemy_text = "None"
                
                if player_class == 1:
                    player_text = "Чародей"
                elif player_class == 2:
                    player_text = "Воин"
                else:
                    player_text = "Разбойник"

                if bot_choice == 1:
                    enemy_text = "Чародей"
                elif bot_choice == 2:
                    enemy_text = "Воин"
                else:
                    enemy_text = "Разбойник"

                rp(f"""[orange3]{"-"*count_underlines*2}[/]\n{' '*12}Результат:\n[orange3]{"-"*count_underlines*2}[/]\n\n""")   
                rp(
                    f"""{' '*3}{name}:{' '*3}{count_space_for_bot}{enemy.name}:\n[orange3]{"-"*(count_underlines)*2}[/]\
                    \n| {' '*len(player_text) if len(player_text) == 4 else ' '*(len(player_text)-6)}{player_text}   | {enemy_text}    |\
                    \n[orange3]{"-"*(count_underlines)*2}[/]\
                    \n| Результат боя: [bold]{who_win}[/]!\
                    \n[orange3]{"-"*(count_underlines)*2}[/]\n
                    """
                    )

                time.sleep(2)
                clear()

            if player_class == 5:

                with open("scores.txt", "a") as file:
                    file.write(f"\n{player.name} | {player.score}")

                check_last = False
                while check_last == False:
                    try:
                        rp(f"""[orange3]{"-"*count_underlines*2}[/]\n{' '*6}[red]Вы проиграли![/] Раунд: {round_game}!\n[orange3]{"-"*count_underlines*2}[/]\n\n""")    
                        rp(
                            f"""[orange3]{"-"*(count_underlines)*2}[/]\n{' '*3}{name}:{' '*3}{count_space_for_bot}{enemy.name}:\n[orange3]{"-"*(count_underlines)*2}[/]\
                            \n| Прогресс: {player.level}   | Прогресс: {enemy.level}    |\
                            \n| Здоровье: {player.lives}   | Здоровье: {enemy.lives}    |\
                            \n| Тв. очки: {player.score}   |                |\
                            \n[orange3]{"-"*(count_underlines)*2}[/]\n
                            """
                            )

                        rp(f"""[orange3]{"-"*count_underlines*2}[/]\n| 1 - Выйти в меню\n[orange3]{"-"*count_underlines*2}[/]\n{' '*4}""")

                        act = int(input("- "))
                        if act == 1:
                            clear()
                            check_last = True
                            stop_limit = False
                            check = True
                            settings.default_settings()
                            game()
                        clear()
                    except:
                        clear()

    if result_action == "rules":
        clear()
        rules()

    if result_action == "top":
        clear()
        leaders()

if __name__ == '__main__':
    try:

        user_name = settings.get_name()
        game()
    
    except KeyboardInterrupt:
        pass

    finally:
        clear()
        rp("До встречи!")