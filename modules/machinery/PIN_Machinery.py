import os
import re
import time
import logging
import subprocess
import os.path

from lib.cuckoo.common.abstracts import Machinery
from lib.cuckoo.common.exceptions import CuckooCriticalError
from lib.cuckoo.common.exceptions import CuckooMachineError

log = logging.getLogger(__name__)


class PINMachinery(Machinery):
	def __init__(self, label):
		self.label = label
	def start(self):
		log.debug("Starting vm %s" % self.label)
		pass
	def stop(self):
		pass
