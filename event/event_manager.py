class event_manager:
	def __init__(self):
		self.events = dict()

	def register_event (self, name, callback):
		if not name in self.events:
			self.events[name] = tuple()
		self.events[name] += (callback,)

	def __call__ (self, name, *params):
		for f in self.events [name]:
			f(*params)

