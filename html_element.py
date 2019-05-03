
# class for every element

class Tag:
	def __init__(self, name, parent = None):
		self.name = name
		self.attrs = {}
		self.text = ''
		self.parent = parent
		self.child = []

	def add_attr(self, key:str, value:str):
		self.attrs[key] = value

	def get_attr(self, key):
		return self.attrs[key]

	def add_to_text(self, text):
		self.text += text

	def append_child(self, new_child):
		self.child.append(new_child)

	def get_child(self):
		return self.child
	
	def find_tag(self,tag):
		if self.name == tag:
			return self
		else:
			children = self.child
			if len(children) > 0:
				while(len(children) > 0):
					cur_child = children.pop()
					if len(cur_child.child) > 0:
						children.extend(cur_child.child)

					if cur_child.name == tag:
						return cur_child	
				
		return None

	
	def find_all(self,tag):
		found = []
		if self.name == tag:
			found.append(self)
		else:
			children = self.child
			if len(children) > 0:
				while(len(children) > 0):
					cur_child = children.pop()
					if len(cur_child.child) > 0:
						children.extend(cur_child.child)

					if cur_child.name == tag:
						found.append(cur_child)	
				
		return found

	def __repr__(self):
		return "name: %s, text: %s \n attrs: %s \n children: %s, " %(self.name, self.text, self.attrs, self.child)