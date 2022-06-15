import unittest
from html_parcer import HtmlParser

class TestHtmlParser(unittest.TestCase):
    def test_get_text_from_html(self):
        parser = HtmlParser()
        test_dictionary = {'index1.html':'123', 'index2.html':'test', 'index3.html':'Text', 'index4.html':'Here is the test', 'index5.html':'My test is here'}
        for key in test_dictionary:
            self.assertCountEqual(parser.getTextFromFile(key), test_dictionary[key])


unittest.main()