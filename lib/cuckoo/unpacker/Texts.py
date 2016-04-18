import platform

ERROR = '\033[91m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
System = platform.system()




def WRITE_ERROR(msg):
	if (System == "Windows"):
		print(msg)
	else:
		print (ERROR + "[-] " +  msg + ENDC)


def WRITE_WARNING(msg):
	if (System == "Windows"):
		print(msg)
	else:
		print (WARNING + "[WARNING]\t" + msg + ENDC)
		
def WRITE_GREEN(msg):
	if (System == "Windows"):
		print(msg)
	else:
		print (OKGREEN + "[+] " + msg + ENDC)

def WRITE_BLUE(msg):
	if (System == "Windows"):
		print(msg)
	else:
		print (OKBLUE +  msg + ENDC)
