import unittest
from html_parser import HtmlParser

class TestHtmlParser(unittest.TestCase):
    def test_get_text_from_html(self):
        parser = HtmlParser()
        test_dictionary = {'test_files\\index1.html':'123', 'test_files\\index2.html':'test', 'test_files\\index3.html':'Text', 'test_files\\index4.html':'Here is the test', 
        'test_files\\index5.html':'My test is here'}
        for key in test_dictionary:
            self.assertCountEqual(parser.getTextFromFile(key), test_dictionary[key])


unittest.main()