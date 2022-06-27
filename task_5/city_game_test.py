import unittest
from city_game import CityGame

class TestCityGame(unittest.TestCase):
    def test_get_city_by_letter(self):
        filename = 'cities_list_test.txt'
        wrong_filename = ''
        letter = 'А'
        answer = 'Александрия'
        digit = 123
        word = 'Киев'

