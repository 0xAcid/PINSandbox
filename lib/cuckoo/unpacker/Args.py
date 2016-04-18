#!/usr/bin/python2.7
import argparse
from os.path import isdir
from VM_Host import VM_Manager
from Texts import WRITE_ERROR, WRITE_WARNING, WRITE_BLUE, WRITE_GREEN

def PINDemoniumArgs():
	
	Parser = argparse.ArgumentParser(description="Automatize PinDemonium and send binaries to CuckooSandbox for a deeper analysis.", )
	# PATH to either file or directory
	Parser.add_argument('-PATH', type=str, help='specify path to file. If you want to scan a directory, add "-d" argument', required=True)
	# PINDemonium arguments
	Parser.add_argument('-iwae', nargs='?', type=int, action='store', metavar='Jumps', help='specify if you want or not to track the inter_write_set analysis dumps and how many jump')
	Parser.add_argument('-antiev', action='store_true', help='specify if you want or not to activate the anti evasion engine')
	Parser.add_argument('-antiev-ins', action='store_true', help='specify if you want or not to activate the single patching of evasive instruction as int2e, fsave...')
	Parser.add_argument('-antiev-sread', action='store_true', help='specify if you want or not to activate the handling of suspicious reads')
	Parser.add_argument('-antiev-swrite', action='store_true', help='specify if you want or not to activate the handling of suspicious writes')
	Parser.add_argument('-unp', action='store_true', help='specify if you want or not to activate the unpacking engine')
	Parser.add_argument('-adv-iatfix', action='store_true', help='specify if you want or not to activate the advanced IAT fix technique')
	Parser.add_argument('-poly-patch', action='store_true', help='if the binary you are analyzing has some kind of polymorphic behavior this activate the patch in order to avoid pin to execute the wrong trace.')
	Parser.add_argument('-nullify-unk-iat', action='store_true', help='specify if you want or not to nullify the IAT entry not detected as correct API by the tool. \033[93mNB: THIS OPTION WILL ACTIVATE adv-iatfix !\033[0m')
	
	Args = Parser.parse_args()	
	if (Args.nullify_unk_iat):
		WRITE_WARNING('You used "-nullify-unk-iat", "-adv-iatfix" will be activated')
		Args.adv_iatfix = True
	Is_Dir = isdir(Args.PATH)
	
	WRITE_GREEN("Will now proceed..")
	Manager = VM_Manager()
	
	
	#try:
		#WRITE_GREEN("Will now proceed..")
	#except:
		#Parser.print_help()
