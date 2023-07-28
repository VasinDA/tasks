from codecs import utf_8_encode

class CityGame:
    def __init__(self, file_name) :
        self.alfabet_str = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                cities_list = file.readlines()
            self.cities_dict = {letter: [city.strip('\n') for city in cities_list if city.startswith(letter)] 
            for letter in self.alfabet_str if len([city.strip('\n') for city in cities_list if city.startswith(letter)]) > 0}
        except IOError:
            raise IOError("Reading file error")

    def getCityByLetter(self, letter):
        if not isinstance(letter, str) or len(letter) > 1:
            return 'Not letter'
        letter = letter.upper()
        if letter not in self.cities_dict:
            return 'No cities starting with this letter'
        for key in self.cities_dict:
            if key == letter:
                if len(self.cities_dict[key]) == 0:
                    return 'Ran out of cities starting with this letter'
                answer_dict = {}
                for i in range(len(self.cities_dict[key])):
                    city = self.cities_dict[key][i]
                    last_letter = city[len(city) - 1].upper()
                    if last_letter in self.cities_dict:
                        if len(self.cities_dict[last_letter]) not in answer_dict:
                            answer_dict[len(self.cities_dict[last_letter])] = i            
                    answer = self.cities_dict[key][answer_dict[min(answer_dict)]]
        new_cities_list = self.cities_dict[letter]
        del new_cities_list[answer_dict[min(answer_dict)]]
        self.cities_dict[letter] = new_cities_list
        return answer