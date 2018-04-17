import unittest
import bib_server

class TestHelper(unittest.TestCase):
	def test_author(self):
		self.assertEqual(bib_server.get_author_list('&Francis&, John'),'John Francis')

	def second_test(self):
		self.assertEqual(bib_server.get_author_list('&D.&, L. E.'),'L. E. D.')

if __name__ == '__main__':
	unittest.main()