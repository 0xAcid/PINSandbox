import argparse



class PINParser:
	
	def __init__(self):
		# Parser is only used to be sure that arguments are right. We keep the string that is in input to use it later.
		# PINDemonium arguments
		self.Parser = argparse.ArgumentParser(description="Automatize PinDemonium and send binaries to CuckooSandbox for a deeper analysis.", )
		self.Parser.add_argument('-iwae', nargs='?', type=int, action='store', metavar='Jumps', default=10, help='specify if you want or not to track the inter_write_set analysis dumps and how many jump (default is 10)' )
		self.Parser.add_argument('-antiev', action='store_true', help='specify if you want or not to activate the anti evasion engine')
		self.Parser.add_argument('-antiev-ins', action='store_true', help='specify if you want or not to activate the single patching of evasive instruction as int2e, fsave...')
		self.Parser.add_argument('-antiev-sread', action='store_true', help='specify if you want or not to activate the handling of suspicious reads')
		self.Parser.add_argument('-antiev-swrite', action='store_true', help='specify if you want or not to activate the handling of suspicious writes')
		self.Parser.add_argument('-unp', action='store_true', help='specify if you want or not to activate the unpacking engine \033[93m(This must be activated, so no choice)\033[0m')
		self.Parser.add_argument('-adv-iatfix', action='store_true', help='specify if you want or not to activate the advanced IAT fix technique')
		self.Parser.add_argument('-poly-patch', action='store_true', help='if the binary you are analyzing has some kind of polymorphic behavior this activate the patch in order to avoid pin to execute the wrong trace.')
		self.Parser.add_argument('-nullify-unk-iat', action='store_true', help='specify if you want or not to nullify the IAT entry not detected as correct API by the tool. \033[93mNB: THIS OPTION WILL ACTIVATE adv-iatfix !\033[0m')
		#self.Parser.add_argument('-timeout', type=int, action="store", default=120, help="Specify timeout for unpacking.", required=False)
	
	def Help(self):
		self.Parser.print_help()
	
	def Parse(self, Data):
		if not Data:
			return
		Args = Data.split(' ')	
		try:
			Args = self.Parser.parse_args(Args)	
		except IOError as e:
			self.Parser.error(e)
			return False
		print(Args)
		if '-unp' not in Data:
			Data = Data + " -unp"
		if (Args.nullify_unk_iat):
			print('\033[93mYou used "-nullify-unk-iat", "-adv-iatfix" will be activated\033[0m')
			if "-adv-iatfix" not in Data:
				Data = Data + " -adv-iatfix"
		return Data
		
	
