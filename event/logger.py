class logger:
	def __init__(self, *log_levels):
		self._log_levels = log_levels

	def __call__(self, log_level):
		def nothing (*args, **kwargs):
			pass

		if not log_level in self._log_levels:
			return nothing

		def log (*args, **kwargs):
			print ('[[', log_level, ']] ', *args, **kwargs)

		return log
