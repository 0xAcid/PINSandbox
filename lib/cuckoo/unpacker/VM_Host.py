#!/usr/bin/python2.7

# We will use Virtual Box python module to exchange file instead of doing it via local network
from time import sleep
import virtualbox
import xmlrpclib
import base64
from Texts import WRITE_ERROR, WRITE_BLUE, WRITE_GREEN, WRITE_WARNING
import subprocess
import zipfile
try:
	from modules.machinery.virtualbox import VirtualBox
except:
	import sys
	sys.path.append('/home/cuckoo/cuckoo')
	from modules.machinery.virtualbox import VirtualBox
	
VM_Name='NECST_PIN_VM'
VB_Manager_PATH='/usr/bin/VBoxManage'
VM_IP = '192.168.56.254'
VM_PORT = 1337
ANALYSIS_TIMEOUT_SECS = 120
MACHINE_START_TIMEOUT = 20

class VM_Manager:
	def __init__(self):
		self.label = VM_Name
		self.mode = "gui" # modify to headless if you don't need GUI
		try:
			self.RestoreSnapShot()			
		except:
			WRITE_ERROR("Error initializing PIN Machine.")
			raise
	
	
	def RestoreSnapShot(self):	
		try:
			proc = subprocess.Popen([VB_Manager_PATH, "snapshot", self.label, "restorecurrent"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			output, err = proc.communicate()
		except OSError as e:
			raise OSError(err)
			
			
	def Send_File(self, PATH, File):
		# Using XMLRPC Server so it can be a remote machine
		WRITE_BLUE("Sending file.")
		Server = xmlrpclib.Server("http://" + VM_IP + ":" + str(VM_PORT))
		with open(PATH, "rb") as handle:
			binary_data = xmlrpclib.Binary(handle.read())
			handle.close()
		Server.Rcv_File(File, binary_data)
		WRITE_GREEN("File sent.")
		

		
	def Rcv_File(self, Filename, ID):
		# Receive file from host
		try:
			WRITE_BLUE("Downloading unpacked binary to : SOMEWHERE")
			Server = xmlrpclib.Server("http://" + VM_IP + ":" + str(VM_PORT))
			
			with open("/home/cuckoo/cuckoo/storage/PINDemonium/" + str(ID) + "/" +Filename + ".zip", "wb") as handle:
				handle.write(base64.b64decode(Server.Send_File()))
				handle.close()
			with zipfile.ZipFile("/home/cuckoo/cuckoo/storage/PINDemonium/" + str(ID) + "/" +Filename + ".zip", "r") as z:
				z.extractall("/home/cuckoo/cuckoo/storage/PINDemonium/" + str(ID) + "/")
		
			
			WRITE_GREEN("File downloaded. Calling Cuckoo.")
			return 
		except OSError as e:
			raise OSError(err)
		
	
	def Start_Unpacking(self, args):
		WRITE_BLUE("Unpacking..")
		Server = xmlrpclib.Server("http://" + VM_IP + ":" + str(VM_PORT))
		Server.Unpack(args)
		WRITE_GREEN("Unpacking done")

		
	def VM_ON(self):
		# Test if VM is already on
		try:
			proc = subprocess.Popen([VB_Manager_PATH, "list", "runningvms"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			output, err = proc.communicate()
			sleep(1)
			if VM_Name in output:
				return 1
			else:
				return 0
				
		except OSError as e:
			raise OSError(err)
			return 0
	
	def start(self):
		# Start and restore snapshot
		TIMEOUT = MACHINE_START_TIMEOUT
		try:
			self.RestoreSnapShot()
			proc = subprocess.Popen([VB_Manager_PATH, "startvm", self.label, "--type", self.mode], stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			WRITE_BLUE("Waiting for VM to start")
			while(True):
				WRITE_BLUE(".")
				if(self.VM_ON()):
					break
				TIMEOUT = TIMEOUT -1
				if not (TIMEOUT):
					WRITE_ERROR("Error starting VM.")
					raise
			WRITE_GREEN("VM ready")
		except OSError as e:
			raise OSError(e)
	
	def stop(self):
		try:
			proc = subprocess.Popen([VB_Manager_PATH, "controlvm", self.label, "poweroff"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			while(True):
				if not(self.VM_ON()):
					break
		except OSError as e:
			raise OSError(err)
		
