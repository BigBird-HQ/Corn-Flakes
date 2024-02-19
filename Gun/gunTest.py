import unittest

from Gun.gun import Gun


class MyTestCase(unittest.TestCase):
    def test_that_magazine_is_empty_at_creation(self):

        gun1 = Gun(0, True)
        self.assertTrue(gun1.check_empty())

    def test_that_when_gun_is_reloaded_adds_bullet_to_magazine(self):

        gun1 = Gun(0, True)
        gun1.reload()
        self.assertEqual(1, gun1.check_magazine())

    def test_that_when_gun_is_reloaded_and_shot_is_fired_magazine_is_empty(self):

        gun1 = Gun(0, True)
        self.assertTrue(gun1.check_empty())
        gun1.reload()
        self.assertEqual(1, gun1.check_magazine())
        gun1.shoot()
        self.assertEqual(0, gun1.check_magazine())

    def test_that_magazine_can_only_contain_seven_bullets_maximum(self):
        gun1 = Gun(0, True)
        self.assertTrue(gun1.check_empty())

        for number in range(1, 8):
            gun1.reload()
        self.assertEqual(7, gun1.check_magazine())

    def test_that_shots_cannot_be_fired_more_times_than_maximum_number_of_bullets_contained_in_magazine(self):

        gun1 = Gun(0, True)
        self.assertTrue(gun1.check_empty())

        for number in range(1, 8):
            gun1.reload()
        self.assertEqual(7, gun1.check_magazine())

        for number in range(1, 8):
            gun1.shoot()
        self.assertEqual(0, gun1.check_magazine())
        


if __name__ == '__main__':
    unittest.main()
