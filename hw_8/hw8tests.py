import unittest
import bib_server

class TestHelper(unittest.TestCase):
	def test_author(self):
		self.assertEqual(bib_server.get_author_list("{{Leavitt}, H.~S.}"),"H. S. Leavitt")

	def second_test(self):
		self.assertEqual(bib_server.get_author_list("{{Pickering}, E.~C.}"),'E. C. Pickering')

if __name__ == '__main__':
	unittest.main()