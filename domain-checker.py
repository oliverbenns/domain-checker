#!/usr/bin/env python3

import subprocess
from config import Config

for name in Config.names:
  for extension in Config.extensions:
    domain = name + '.' + extension
    proc = subprocess.Popen(["whois", domain], stdout=subprocess.PIPE)
    output = proc.stdout.read()
    proc.wait()

    # TypeError: a bytes-like object is required, not 'str'
    taken = "No match for" in output

    if taken:
      print("domain is taken.")
    else:
      print("domain is available.")
