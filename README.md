# Domain Checker
Tool to check if domains are available.

## Pseudo / Todo

- Store array of wanted keywords (e.g. google, microsoft, facebook)
- Store array of wanted extensions (e.g. com, co.uk, net)

- For each keyword in keywords
  - for each extension in extensions
    - Do a whois lookup for keyword + extension
    - Analyse whois lookup response
    - If available
      - stdout > "Domain _ is available"
      - notify (email? apple notification? run a bash script?)
    - Else
      - Nothing
