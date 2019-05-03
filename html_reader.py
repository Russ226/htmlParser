#open html
#begin reading line by line # stack for '<' and '>' and a stack for html elements
from html_parser.html_element import Tag
# from html_element import Tag

quick_run_file = 'test1.html'
 
def read_html(file_name):
	file = open(file_name ,'r')
	html = ''
	for line in file:
		html+=line


	file.close()
	return html

def check_html_line(html):
	if html[0] == '<':
		return False
	return True

def check_useless(body):
	if body == '\n' or body == '':
		return True

	#ignore comments
	if body[0] == '<' and body[1] == '!':
		return True



	return False

def create_cur_tag(body, cur):
	if body[0] == '<' and body[1] != '/' and not check_useless(body):
		whole_tag = body.split(' ')
		body = whole_tag[0][1:]
		if cur != None:
			cur.append_child(Tag(body, cur))		
			cur = cur.get_child()[-1]
			cur = parse_attributes(whole_tag,cur)
		else:
			cur = Tag(body, cur)
			cur = parse_attributes(whole_tag,cur)

	return body,cur

def parse_attributes(body, cur):
	for attr in body:
		key_value = attr.split('=')
		if len(key_value) == 2:
			cur.add_attr(key_value[0],key_value[1].replace('"',''))

	return cur

def parser(html):
	html_list = html.split(">")

	cur = None
	for body in html_list:
		body = body.replace('\n\t', '')
		body = body.replace('\n', '')
		body = body.replace('\n\n\t', '')

		if not check_useless(body):
			if not check_html_line(body):
				body, cur = create_cur_tag(body,cur)
			else:
				counter = 0
				for char in body:
					if char == '<':
						body,cur = create_cur_tag(body[counter:],cur)
						break
					else:
						cur.add_to_text(char)

					counter += 1
			## parse closing tag
			if len(body) > 1 and body[1] == '/' and cur.parent != None:
				cur = cur.parent
		else:
			print(body)
				
	
	return cur



# html = read_html(quick_run_file)
# cur = parser(html)
# print(cur)



## going to try parsing it like it was in string instead of lines

# split by space(maybe change it to char by char parse instead of string by string)
# loop through string
# track opening brackets and closing
# text between opeing and closing tag
# 	text starts after closing bracker of opening tag and lasts till opening tag of another element	


		