import os, random
import settings as st
import game_exceptions

class Enemy:
    def __init__(self, level, name):
        self.level = level
        self.lives = st.ENEMY_LIVES
        self.name = name

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        if self.lives > 1 or st.ENEMY_LIVES > 1:
            st.minus_enemy_lives()
            if st.ENEMY_LIVES == 0:
                exc = game_exceptions.EnemyDown()
                exc.regenerate_enemy()
        else:
            exc = game_exceptions.EnemyDown()
            exc.regenerate_enemy()

class Player:
    def __init__(self, name, lives, score, level, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
        self.level = level
        self.allowed_attacks = allowed_attacks


    @staticmethod
    def fight(attack, defence):
        """
        return 0 - Ничья
        return -1 - Победил тот кто нападал (защита не удачная)
        return 1 - Победил тот кто защищался (атака не удачная)
        """

        if attack == defence:
            return 0

        elif attack == 1 and defence == 2:
            return -1

        elif attack == 2 and defence == 3:
            return -1

        elif attack == 3 and defence == 1:
            return -1

        elif attack == 2 and defence == 1:
            return 1

        elif attack == 3 and defence == 2:
            return 1

        elif attack == 1 and defence == 3:
            return 1

        else:
            return 0

    def attack(self, player_choice, bot_choice):
        result_attack = Player.fight(player_choice, bot_choice)
        if result_attack == 0:
            return result_attack
        elif result_attack == -1:
            Enemy.decrease_lives(self)
            st.PLAYER_SCORE += 1
        elif result_attack == 1:
            st.minus_player_lives()
            rs = game_exceptions.GameOver()
            rs.check_game_status(st.COUNT_LIVES)

        return result_attack


    def defence(self, bot_choice, player_choice):
        result_defence = Player.fight(bot_choice, player_choice)
        if result_defence == 0:
            return result_defence
        elif result_defence == -1:
            st.minus_player_lives()
            rs = game_exceptions.GameOver()
            rs.check_game_status(st.COUNT_LIVES)
        elif result_defence == 1:
            Enemy.decrease_lives(self)
            st.PLAYER_SCORE += 1

        return result_defence