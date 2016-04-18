from Texts import WRITE_BLUE, WRITE_ERROR
from VM_Host import VM_Manager
import datetime
import os
def Unpack(options):
	# Check if PINDemonium directory already exiists
	if not os.path.exists("/home/cuckoo/cuckoo/storage"):
		os.makedirs("/home/cuckoo/cuckoo/storage")
	if not os.path.exists("/home/cuckoo/cuckoo/storage/PINDemonium"):
		os.makedirs("/home/cuckoo/cuckoo/storage/PINDemonium")	
	
	WRITE_BLUE("Unpacking process")

	Manager = VM_Manager()
	# We transfer every PIN arguments via one of cuckoo arguments. we will restore it to the original later.
	# Doing this we avoid changing all the code.
	PINArgs = options["package"].split(";")[1]
	print(PINArgs)
	
	if(Manager.VM_ON()):
		Manager.stop()	
	Manager.start()
	Manager.Send_File(options['target'], options["file_name"])
	
	print(Manager.Start_Unpacking(PINArgs))
	
	# Downloading report + unpacked binary
	if not os.path.exists("/home/cuckoo/cuckoo/storage/PINDemonium/" + str(options['id'])):
		os.makedirs("/home/cuckoo/cuckoo/storage/PINDemonium/" + str(options['id']))
	Manager.Rcv_File(options['file_name'], options['id'])
	
	if os.path.exists("/home/cuckoo/cuckoo/storage/PINDemonium/" +  str(options['id'])  + "/unpacked.exe"):
		options["target"] = "/home/cuckoo/cuckoo/storage/PINDemonium/" +  str(options['id'])  + "/unpacked.exe"
		options["file_name"] = "unpacked.exe"
	else:
		#Error with the binary. Cannot be unpacked.
		WRITE_ERROR("Error unpacking the file, analyzing original file with cuckoo.\n")
	options["package"] = 'exe'
	Manager.stop()
	return options


if __name__ == '__main__':
	print("DEbug purpose")
	options = {'category': u'file', 'target': u'/home/squall/Bureau/nc.exe', 'package': u'exePIN;-antiev -iwae 10', 'file_type': 'PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows', 'file_name': u'nc.exe', 'clock': datetime.datetime(2016, 4, 13, 16, 30, 36, 200532), 'id': 18, 'terminate_processes': False, 'options': 'apk_entry=:', 'enforce_timeout': False, 'timeout': 120, 'ip': u'192.168.56.1', 'pe_exports': '', 'port': u'2042'}
	Unpack(options)
