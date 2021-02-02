import re

time_pattern="time=[0-9]*.[0-9]*"

def parse_ping_output(ping_output):
  time_value = re.findall(time_pattern, ping_output)[0].split('=')[1]
  return time_value
