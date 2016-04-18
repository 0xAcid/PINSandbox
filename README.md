![Cuckoo](http://cuckoosandbox.org/graphic/cuckoo.png)

In three words, [Cuckoo Sandbox](http://www.cuckoosandbox.org) is a malware analysis system.

What does that mean? It simply means that you can throw any suspicious file at it and in a matter of seconds Cuckoo will provide you back some detailed results outlining what such file did when executed inside an isolated environment.

If you want to contribute to development, please read [this](http://www.cuckoosandbox.org/development.html) and [this](http://www.cuckoofoundation.org/contribute.html) first. Make sure you check our Issues and Pull Requests and that you join our IRC channel.

<hr />

This is a development version, we do not recommend its use in production.

You can find a full documentation of the latest stable release [here](http://docs.cuckoosandbox.org).

<hr />

[![Build Status](https://travis-ci.org/cuckoosandbox/cuckoo.png?branch=master)](https://travis-ci.org/cuckoosandbox/cuckoo)
# PINSandbox

## Dependencies
 * PINSandbox is using VirtualBox only (no specific version)

PINSandbox is a Cuckoo Sandbox mod which integrates [PINDemonium](https://github.com/Seba0691/PINdemonium).
1. Clone this repository, install and configure everything like you would have for a simple CuckooSandbox.
2. Install a machine that can run [PINDemonium](https://github.com/Seba0691/PINdemonium) with all dependencies.
3. Upload the file PINSandbox/PINAgent/Agent.py to the PIN machine, run it and take a snapshot. (You can configure IP, port and timeout of the unpacking in it)
4. Almost everything that is used for PINSandbox is in PINSandbox/lib/cuckoo/unpacker/ . 
5. Modify variables in PINSandbox/lib/cuckoo/unpacker/VM_Host.py (VM_Name, VB_Manager_PATH, VM_IP, VM_PORT, MACHINE_START_TIMEOUT)
6. Send your file to cuckoo sandbox using  PINSandbox/utils/submit.py (it is a modified version)
7. You can either force PINDemonium to be un by specifying "--PIN" or let the tool determine if the file needs unpacking (Entropy > 7.5)
