import os, settings

class GameOver():
    def __init__(self):
        pass

    @staticmethod
    def check_game_status(count_leaves):
        if count_leaves <= 0:
            settings.game_over()

class EnemyDown():
    def __init__(self):
        pass

    @staticmethod
    def regenerate_enemy():
        settings.generate_enemy()
        settings.action_after_kill()