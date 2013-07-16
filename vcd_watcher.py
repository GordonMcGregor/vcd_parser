class VcdWatcher(object):

	sensitive = []
	watching = []
	trackers = []
	default_hierarchy = None

	_sensitive_ids = []
	_watching_ids = []

	def __init__(self):
		pass


	def update(self, changes):
		
		if self.start_tracker(changes):
			self.trackers.append(self.create_new_tracker(changes))

		for tracker in self.trackers:
			tracker.update(changes)

		for tracker in self.trackers:
			if tracker.finished:
				self.trackers.remove(tracker)


	def start_tracker(self, changes):
		return False


	def update_ids(self, vcd):		
		_sensitive_ids = [vcd.get_id(xmr) for xmr in self.sensitive]
		_watching_ids = [vcd.get_id(xmr) for xmr in self.watching]


	def set_hierarchy(self, hierarchy):
		self.default_hierarchy = hierarchy


	def add_sensitive(self, signal, hierarchy=None):
		if not hierarchy:
			hierarchy = self.default_hierarchy
		self.sensitive.append(hierarchy + '.' + signal)


	def add_watching(self, signal, hierarchy=None):
		if not hierarchy:
			hierarchy = self.default_hierarchy
		self.watching.append(hierarchy + '.' + signal)





class VcdTracker(object):

	finished = False

	def __init__(self):
		pass

	def update(self, changes):
		pass

