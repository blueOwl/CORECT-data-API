import json
import sys

args = sys.argv
f = args[-1]
kvs = args[1:-1]
req = {}
for i in kvs:
	l = i.split("=")
	k, v = l[0], l[1]
	req[k] = v
config = json.load(open(f))
for i in config:
	req[i] = config[i]

s = json.dump(req, open("tmp.json","w"))
