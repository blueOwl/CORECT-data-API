import pysam

indexed_data_set = {}
for i in range(1,23):
	indexed_data_set[i] = pysam.TabixFile("data/chr" +  str(i) + ".tsv.vcf.sorted.gz")

def region_q(chrom, start, end):
	data = []
	try:
		for row in indexed_data_set[chrom].fetch(str(chrom), start, end):
			data.append(str(row))
	except:
		pass
	return data
		
def var_q(chrom, pos, ref, alt):
	if ref:
		try:
			for row in indexed_data_set[chrom].fetch(str(chrom), pos - 1, pos):
				line = row.split("\t")
				if line[3] == ref and line[4] == alt:
					return [row]
			return []
		except:
			return []
	else:
		data = []
		try:
			for row in indexed_data_set[chrom].fetch(str(chrom), pos - 1, pos):
				data.append(row)
		except:pass
		return data
		

