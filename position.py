class Position:
	def __init__(self, idx, txt):
		self.idx = idx
		self.ftxt = txt

	def advance(self, current_char=None):
		self.idx += 1

		return self
        

	def copy(self):
		return Position(self.idx, self.ln, self.col, self.ftxt)