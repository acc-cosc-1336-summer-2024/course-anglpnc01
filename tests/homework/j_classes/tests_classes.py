import unittest


from src.homework.j_classes.class_a import die, roll


class Test_Config(unittest.TestCase):

    def test_get_rolled_value(self):
        
        roll_value = die.roll()

        self.assertEqual(True, roll() >= 1)
        self.assertEqual(True, roll() <= 12)