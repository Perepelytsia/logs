class Parser:
	"""docstring"""
	post    = ''
	trace   = None

	def __init__(self, day, request):
		"""Constructor"""
		self.day     = day[1:-10]
		self.request = request.strip()

	def addPost(self, post):
		self.post += post.strip()

	def addTrace(self, trace):
		self.trace = trace

	def getData(self):
		return [self.day, self.request, self.post, self.trace]
