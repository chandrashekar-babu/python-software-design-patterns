import re
import csv


regex = r'''
  (?P<time>   # Extract timestamp (Dec 30 06:00:23)
     \w+      
     \s       
     \d+
     \s
     \S+       
  )
  .+
  Failed
  \s
  password
  \s
  for
  \s
  (invalid \s user \s)?
  (?P<username>\S+?)     # Extract username
  \s from \s
  (?P<ipaddr>\S+)        # Extract ip address
'''
pattern = re.compile(regex, re.VERBOSE)

with open("sshd_minimal.log", "r") as ins, \
    open("failed_logins.csv", "w") as outs:
        csvout = csv.DictWriter(outs, fieldnames=tuple(pattern.groupindex.keys()))
        csvout.writeheader()
        for line in ins:
            if m := pattern.search(line):
                print(csvout.writerow(m.groupdict()))

