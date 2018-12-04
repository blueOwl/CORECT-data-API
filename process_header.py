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
	def get_detail(self):
		return self.exp + self.details
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
class Tree_node:
	id = 0
	def __init__(self, name = '', detail = None, parent_id = 0):
		self.id = Tree_node.id
		self.name = name
		self. detail = detail
		self.parent_id = parent_id
		Tree_node.id += 1
	def get_node_dic(self):
		return {'id':self.id, 'name':self.name, 'detail':self.detail, 'parent_id':self.parent_id}
tree_array = []
tree_array.append(Tree_node(name = 'root', parent_id = None).get_node_dic())
for i in single:
	tree_array.append(Tree_node(name = i, detail = anno_dic[i].get_detail()).get_node_dic())
for i in dup_dic:
	p = Tree_node(name = i)
	tree_array.append(p.get_node_dic())
	for k in dup_dic[i]:
		tree_array.append(Tree_node(name = k, detail = anno_dic[k].get_detail(), parent_id = p.id).get_node_dic())

if __name__ == "__main__":
	print single
	print dup_dic
	print tree_array
