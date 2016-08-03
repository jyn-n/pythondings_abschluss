from .log import event

class event_manager:
	def __init__(self, logger):
		self._events = dict()
		self._logger = logger

	def register_event (self, name, callback):
		self._logger(event)("registering", callback.__name__, "to <<", name, ">>")
		if not name in self._events:
			self._events[name] = tuple()
		self._events[name] += (callback,)

	def __call__ (self, name, *params):
		self._logger(event)("calling <<", name, ">> with:", " , ".join(map (lambda x: type(x).__name__ + ':' + str(x) , params)))
		if name not in self._events: return None
		for f in self._events [name]:
			a = f(*params)
		return a

