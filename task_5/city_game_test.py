import unittest
from city_game import CityGame

class TestCityGame(unittest.TestCase):
    def test_get_city_by_letter(self):
        wrong_filename = ''
        filename = 'test_file//cities_list_test.txt'
        digit = 123
        word = 'Киев'
        test_letter = 'А'
        test_answer = 'Александрия'
        test_last_value_letter = 'Я'
        test_last_value_answer = 'Ялта'
        start_game = CityGame(filename)
        len_list_cities_a = start_game.cities_dict[test_letter]
        with self.assertRaisesRegex(IOError, 'Reading file error'):
            start_game_error = CityGame(wrong_filename)
        self.assertEqual(start_game.getCityByLetter(digit), 'Not letter')
        self.assertEqual(start_game.getCityByLetter(word), 'Not letter')
        self.assertEqual(start_game.getCityByLetter(test_letter), test_answer)
        self.assertNotEqual(len_list_cities_a, len(start_game.cities_dict[test_letter]))
        self.assertEqual(start_game.getCityByLetter(test_last_value_letter), test_last_value_answer)
        self.assertEqual(start_game.getCityByLetter(test_last_value_letter), 'Ran out of cities starting with this letter')

unittest.main()
        

