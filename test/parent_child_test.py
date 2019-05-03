import unittest
import sys
sys.path.insert(0, '../')
import html_parser.html_reader as hr

class TestReadingMoreComplexFiles(unittest.TestCase):
	
	def setUp(self):
		self.html = hr.read_html("test/html/innerhtml1.html")
		self.result = hr.parser(self.html)

	
	def test1(self):
		h1Tag = self.result.child[0]
		self.assertTrue('h1' == h1Tag.name)
		self.assertTrue('Things I\'ve learned' == h1Tag.text)
	
	def test2(self):
		olTag = self.result.child[2]

		self.assertTrue('ol' == olTag.name)
		self.assertTrue('li' == olTag.child[0].name)
		self.assertTrue('HTTP Requests' == olTag.child[0].text)
		self.assertTrue('li' == olTag.child[1].name)
		self.assertTrue('IP address' == olTag.child[1].text)
		self.assertTrue('li' == olTag.child[2].name)
		self.assertTrue('Servers' == olTag.child[2].text)

class TestFindFunction(unittest.TestCase):
	
	def setUp(self):
		self.html = hr.read_html("test/html/innerhtml1.html")
		self.result = hr.parser(self.html)

	
	def test_find_h1(self):
		h1Tag = hr.Tag.find_tag(self.result, 'h1')

		self.assertTrue('h1' == h1Tag.name)
		self.assertTrue('Things I\'ve learned' == h1Tag.text)
	
	def test_find_em(self):
		emTag = hr.Tag.find_tag(self.result, 'em')

		self.assertTrue('em' == emTag.name)
		self.assertTrue('em' == emTag.text)

	def test_find_all_h1(self):
		h1Tag = self.result.find_all('h1')
		
		self.assertTrue(1 == len(h1Tag))
		self.assertTrue('h1' == h1Tag[0].name)
		self.assertTrue('Things I\'ve learned' == h1Tag[0].text)
	
	def test_find_all_li(self):
		liTag = self.result.find_all('li')
		
		self.assertTrue(15 == len(liTag))
		self.assertTrue('HTTP Requests' == liTag[-1].text)
		self.assertTrue('IP address' == liTag[-2].text)
		self.assertTrue('Servers' == liTag[-3].text)
	
	def test_find_all_li(self):
		strongTag = self.result.find_all('strong')

		self.assertTrue(2 == len(strongTag))
		self.assertTrue('Hyper text Markup Language' == strongTag[-1].text)
		self.assertTrue('strong' == strongTag[-2].text)

if __name__ == '__main__': 
    unittest.main() 
