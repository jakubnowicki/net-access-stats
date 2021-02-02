import os
import time
from pingstats.parser import parse_ping_output

write_file = "output.csv"

with open(write_file, "w") as output:
    for _ in range(10):
        ping = os.popen("ping -c 1 google.com").read()
        output.write("google.com, " + parse_ping_output(ping) + "\n")
        time.sleep(1)
