from codecs import utf_8_encode


class CityGame:
    def readCitiesFromFile(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                cities_list = file.readlines()
            return cities_list
        except IOError:
            raise IOError("Reading file error")

    def getCityFromList(letter):
        letter = letter.upper()
        