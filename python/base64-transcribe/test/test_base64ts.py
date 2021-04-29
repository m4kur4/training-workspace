import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mod_base64ts import fuga
# 間違い： import mod_base64ts.fuga
# 間違い： import mod_base64ts
# 間違い： from mod_base64ts import *

class TestStringMethods(unittest.TestCase):

	def test_str_to_bin(self):
		expected = ''
		# actual = mod_base64ts.hoge.str_to_bin('hoge')
		actual = fuga.do_fuga()
		self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()