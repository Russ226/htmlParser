import unittest
import sys
sys.path.insert(0, '../')
import html_parser.html_reader as hr

class TestParsingAttr(unittest.TestCase):
	
	def setUp(self):
		self.html = hr.read_html("test/html/testattr1.html")
		self.result = hr.parser(self.html)

	
	def test1(self):
		self.assertTrue('p' == self.result.child[0].child[0].name)
		self.assertTrue('checking' == self.result.child[0].child[0].text)
		self.assertTrue('one' == self.result.child[0].child[0].get_attr('id'))
		self.assertTrue('bye' == self.result.child[0].child[0].get_attr('class'))
	

if __name__ == '__main__': 
    unittest.main() 