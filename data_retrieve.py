import pysam
import config
import json
import re

indexed_data_set = {}
def get_symbol_position():
	d = json.load(open(config.GENE_REGION_FILE))
	return {str(k):d[k] for k in d}

symbol_positions = get_symbol_position()
for i in range(1,23):
	indexed_data_set[i] = pysam.TabixFile("data/chr" +  str(i) + ".tsv.vcf.sorted.gz")

def region_q(header_index, chrom, start, end):
	data = []
	try:
		for row in indexed_data_set[chrom].fetch(str(chrom), start, end):
			line = str(row).split("\t")
			data.append([line[i] for i in header_index])
	except:
		pass
	return data
		
def var_q(header_index, chrom, pos, ref, alt):
	data = []
	if ref and alt:
		ref, alt = str(ref), str(alt)
		try:
			for row in indexed_data_set[chrom].fetch(str(chrom), pos - 1, pos):
				line = str(row).split("\t")
				if line[3] == ref and line[4] == alt:
					data.append([line[i] for i in header_index])
		except:
			return []
	return data

def gene_region(s):
	keys = []
	for i in symbol_positions:
		if re.search(s, i, re.IGNORECASE):
			keys.append(i)
	return {i:symbol_positions[i] for i in keys}
	
		

if __name__ == "__main__":
	print region_q([0,1,3,4], 2, 100007, 101119)
	print var_q([0,1,3,4], 2, 100008, "T", "A")
	print gene_region("RNY1P13")
