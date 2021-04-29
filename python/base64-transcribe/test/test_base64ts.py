import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mod_base64ts

class TestStringMethods(unittest.TestCase):

	def test_str_to_bin(self):
		expected = ''
		actual = mod_base64ts.str_to_bin('hoge')
		self.assertEqual(actual, expected)

if __name__ == '__main__':
	print(mod_base64ts.BYTE_SIZE)
	unittest.main()