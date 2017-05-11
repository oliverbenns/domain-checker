#!/usr/bin/env python3

import subprocess
from config import Config
from colors import Colors
from notify import notify

for name in Config.names:
  for extension in Config.extensions:
    domain = name + '.' + extension

    process = subprocess.Popen(["whois", domain], stdout=subprocess.PIPE)
    output = process.stdout.read();

    available = b"No match for" in output

    if available:
      print(Colors.success + "Domain available: " + domain + Colors.none)
      notify(domain)
    else:
      print(Colors.fail + "Domain taken: " + domain + Colors.none)

