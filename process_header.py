import config
skip_items = config.SKIP_ITEMS
f = open(config.HEADER_DESP)
f.readline()

class Anno:
	def __init__(self, key):
		self.key = key
		self.exp = ''
		self.details = ''
	def __str__(self):
		return self.key
anno_dic = {}
for i in f:
	if len(i.rstrip().split()) == 0:continue
	if i[0] != "\t":continue
	if i[:2] == "\t\t":
		if key: anno_dic[key].details += i.rstrip()
		else:print(i)
	else:
		l = i[1:].rstrip().split(':')
		key = l[0]
		anno_dic[key] = Anno(key)
		anno_dic[key].exp = l[1]
#for i in sorted(anno_dic):
#	print(i)
for k in [i for i in anno_dic]:
	if k in skip_items:anno_dic.pop(k, None) 
single = []
dup_dic = {}
for i in sorted(anno_dic):
	if "_" not in i:
		single.append(i)
	else:
		start = i.split("_")[0]
		c = 0
		for a in anno_dic:
			if start+'_' in a : c+= 1
		if c < 2:
			single.append(i)
		else:
			if dup_dic.get(start):
				dup_dic[start].append(i)
			else:
				dup_dic[start] = [i]
