#!/usr/bin/env python3

import subprocess
import time

def notify(domain):
  # Mac notification
  command = "osascript '-e display notification \"" + domain + "\" with title \"Domain available\"'"
  subprocess.call(command, shell=True)
  # Can't find a way to stack these so setting slight delay incase user doesn't see one
  time.sleep(2)
