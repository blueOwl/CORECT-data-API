from process_header import tree_array, anno_dic

def make_id_header_map(tree_array):
	id_map = {}
	for i in tree_array:
		if i['name'] in anno_dic:
			id_map[str(i['id'])] = i['name']
	return id_map

header_id_map = make_id_header_map(tree_array)
if __name__ == "__main__":
	print(make_id_header_map(tree_array)) 


