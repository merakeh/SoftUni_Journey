import unittest
from hero.project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_initializing(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_when_hero_is_the_same_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_without_any_health_points_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError)as ve:
            self.hero.battle(self.enemy)

        expected_result = "Your health is lower than or equal to 0. You need to rest"

        self.assertEqual(expected_result, str(ve.exception))

    def test_try_battling_when_enemys_health_is_not_enough_raise_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError)as ve:
            self.hero.battle(self.enemy)

        expected_result = f"You cannot fight Enemy. He needs to rest"
        self.assertEqual(expected_result, str(ve.exception))

    def test_health_remove_after_battle_is_draw_expect_correct(self):
        self.hero.health = 50
        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_enemy_and_win_expect_stats_increase(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_enemy_and_lose_expect_stats_decrease(self):
        self.hero, self.enemy = self.enemy, self.hero
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_correct__str__method(self):
        expected_result = f"Hero Hero: 1 lvl\n" \
                          f"Health: 100\n" \
                          f"Damage: 100\n"

        result = str(self.hero)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()