import unittest
import sys
sys.path.insert(0, '../')
import html_parser.html_reader as hr

class TestIgnoringComments(unittest.TestCase):
	
	def setUp(self):
		self.html = hr.read_html("test/html/testcomments.html")
		self.result = hr.parser(self.html)

	
	def test1(self):
		print(self.result.child)
		self.assertTrue('body' == self.result.name)
		self.assertTrue('' == self.result.text)
		self.assertTrue('ol' == self.result.child[2].name)
		

class TestIgonoringDoctypeHeading(unittest.TestCase):
	
	def setUp(self):
		self.html = hr.read_html("test/html/testcomments.html")
		self.result = hr.parser(self.html)

	
	def test1(self):
		print(self.result.child)
		self.assertTrue('body' == self.result.name)
		self.assertTrue('' == self.result.text)
		self.assertTrue('ol' == self.result.child[2].name)
		
	

if __name__ == '__main__': 
    unittest.main() 