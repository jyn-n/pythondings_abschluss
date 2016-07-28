class event_manager:
	def __init__(self, logger):
		self._events = dict()
		self._logger = logger

	def register_event (self, name, callback):
		self._logger('events')("registering", callback.__name__, "to <<", name, ">>")
		if not name in self._events:
			self._events[name] = tuple()
		self._events[name] += (callback,)

	def __call__ (self, name, *params):
		self._logger('events')("calling <<", name, ">> with:", *map (str, params))
		for f in self._events [name]:
			a = f(*params)
		return a

