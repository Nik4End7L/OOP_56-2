class HC:

	def __init__(self, initials, time, specials):
		self.initials = initials
		self.time = time
		self.specials = specials 

	def someinfo(self):
		return print(f'Name {self.initials}; Time(Begining of reign) {self.time} y; Specials {self.specials}.')

AH = HC('A.H', 1939, 'Artist')
AH.someinfo()
WC = HC('W.C', 1945, 'Nobel prize in literature')
WC.someinfo()