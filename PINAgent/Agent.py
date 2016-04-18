from SimpleXMLRPCServer import SimpleXMLRPCServer
import base64
import subprocess
from os import chdir
from os import listdir
import zipfile
BIND_IP = "0.0.0.0"
BIND_PORT = 1337
TIMEOUT = 120

class Agent:

        def __init__(self):
                self.server = SimpleXMLRPCServer((BIND_IP, BIND_PORT))
                self.server.register_function(self.Rcv_File, 'Rcv_File')
                self.server.register_function(self.Send_File, 'Send_File')
                self.server.register_function(self.Unpack, 'Unpack')
                self.server.serve_forever()
                self.PATH = None
                self.server.timeout = TIMEOUT


                
        def Rcv_File(self, filename, bdata):
                with open("C:\\Users\\andrea\\Desktop\\" + filename, "wb") as handle:
                        try:
                                handle.write(bdata.data)
                                handle.close()
                                self.PATH = "C:\\Users\\andrea\\Desktop\\" + filename
                                return 1
                        except:
                                return 0
                        
                        
        def Unpack(self, flags):
				flags = flags.split(" ")
				SubFlags = ["pin.exe", "-t", "PINDemonium.dll"]
				for i in flags:
					SubFlags.append(i)
				SubFlags.append("--")
				SubFlags.append(self.PATH)
                if self.PATH:
                        try:
                                chdir("C:\\pin")
                                proc = subprocess.Popen(SubFlags, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                output, err = proc.communicate()
                                print("Looks like we are done")
                                print(output)
                                print(err)
                                return output
                        except:                               
                                print("ERROR executing PINDemonium")
                                return -1
                else:
                        print("NO PATH")
                        return -1
                        

        def Send_File(self):
                try:
						chdir("C:\\pin\\PinUnpackeResults\\")
                        Results = "C:\\pin\\PinUnpackerResults\\" + listdir("C:\\pin\\PinUnpackerResults")[0]
                        Files = listdir(Results)
                        zipf = zipfile.ZipFile("Results.zip", 'w', zipfile.ZIP_DEFLATED)
                        for i in Files:
                                if ".txt" in i:
                                        zipf.write(Results + "\\" + i, arcname=i)
                                elif ".exe" in i:
                                        zipf.write(Results + "\\" +  i, arcname="unpacked.exe")
                                else:
                                        print(i)
                        zipf.close()
                        
                        with open("C:\\pin\\PinUnpackerResults\\Results.zip", "rb") as handle:
                                return base64.b64encode(handle.read())
                except:
                        return base64.b64encode("ERROR")


Ag = Agent()
