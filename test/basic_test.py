import unittest
import sys
sys.path.insert(0, '../')
import html_parser.html_reader as hr

class TestReadingTag(unittest.TestCase):
	## each test reads from a different html file 
	## parses the right tag

	def test1(self):
		html = hr.read_html("test/html/test1.html")
		result = hr.parser(html)

		self.assertTrue('p' == result.name) 

	def test2(self):
		html = hr.read_html("test/html/test2.html")
		result = hr.parser(html)

		self.assertTrue('p' == result.name) 

	def test3(self):
		html = hr.read_html("test/html/test3.html")
		result = hr.parser(html)

		self.assertTrue('p' == result.name) 


class TestReadingInnerTag(unittest.TestCase):
	## each test reads from a different html file 
	## parses the right tag

	def test1(self):
		self.html = hr.read_html("test/html/testinner1.html")
		self.result = hr.parser(self.html)

		self.assertTrue('span' == self.result.child[0].name)
		self.assertTrue(1 == len(self.result.child)) 


	def test2(self):
		self.html = hr.read_html("test/html/testinner2.html")
		self.result = hr.parser(self.html)

		self.assertTrue('span' == self.result.child[0].name)
		self.assertTrue(1 == len(self.result.child))
		 


	def test3(self):
		self.html = hr.read_html("test/html/testinner3.html")
		self.result = hr.parser(self.html)
		
		self.assertTrue('span' == self.result.child[0].name)
		self.assertTrue(1 == len(self.result.child))

	

class TestchildParentRelations(unittest.TestCase):
	## each test reads from a different html file 
	## parses the right tag

	def test1(self):
		self.html = hr.read_html("test/html/childparenttest.html")
		self.result = hr.parser(self.html)

		self.assertTrue('p' == self.result.child[0].name) 
		self.assertTrue('p' == self.result.child[1].name)
		self.assertTrue('div' == self.result.name) 


	def test_unordered_list(self):
		self.html = hr.read_html("test/html/unorderedlist.html")
		self.result = hr.parser(self.html)

		self.assertTrue('body' == self.result.name) 
		self.assertTrue('ul' == self.result.child[0].name) 
		self.assertTrue('li' == self.result.child[0].child[0].name)
		self.assertTrue('1' == self.result.child[0].child[0].text) 
		self.assertTrue('li' == self.result.child[0].child[3].name)
		self.assertTrue('4' == self.result.child[0].child[3].text) 

	



if __name__ == '__main__': 
    unittest.main() 