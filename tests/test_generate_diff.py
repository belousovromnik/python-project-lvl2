import unittest

from gendiff.engine import generate_diff

class TestGenerate_Diff(unittest.TestCase):

    def test_instantiation(self):
        first_file = '/home/belrom/python-project-lvl2/before.json'
        second_file = '/home/belrom/python-project-lvl2/after.json'
        assert_diff = '''
{\n
    host: hexlet.io\n
  + verbose: True\n
  - timeout: 50\n
  + timeout: 20\n
  - proxy: 123.234.53.22\n
}'''
        diff = generate_diff(first_file, second_file)
        self.assertEqual(diff, assert_diff)
