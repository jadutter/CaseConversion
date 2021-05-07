import unittest
from case_parse import parseVariable

class TestCaseParse(unittest.TestCase):
    def _test_case_parse(self, parseVar, expect, detectAcronyms=True, acronyms=[], preserveCase=False):
        result = parseVariable(parseVar, detectAcronyms=detectAcronyms, acronyms=acronyms, preserveCase=preserveCase)
        self.assertEqual(result, expect)

    def test_snake_case(self):
        self._test_case_parse('snake_case',(['Snake', 'Case'],  'lower', '_'))

    def test_screaming_snake_case(self):
        self._test_case_parse('SCREAMING_SNAKE_CASE',(['Screaming', 'Snake', 'Case'],  'upper', '_'))

    def test_camel_case(self):
        self._test_case_parse('camelCase',(['Camel', 'Case'],  'camel', False))
    
    def test_pascal_case(self):
        self._test_case_parse('PascalCase',(['Pascal', 'Case'],  'pascal', False))

    def test_dot_case(self):
        self._test_case_parse('dot.case',(['Dot', 'Case'],  'lower', '.'))

    def test_dash_case(self):
        self._test_case_parse('dash-case',(['Dash', 'Case'],  'lower', '-'))
    
    def test_slash_case(self):
        self._test_case_parse('slash/case',(['Slash', 'Case'],  'lower', '/'))

    def test_backslash_case(self):
        self._test_case_parse('backslash\\case',(['Backslash', 'Case'],  'lower', '\\'))

    def test_title_case(self):
        self._test_case_parse('Title Case',(['Title', 'Case'],  'pascal', ' '))

    def test_separate_words(self):
        self._test_case_parse('separate words',(['Separate', 'Words'],  'lower', ' '))




if __name__ == '__main__':
    unittest.main()