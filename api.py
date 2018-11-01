from flask import Flask, request, send_from_directory, jsonify, abort
from functools import wraps
from data_retrieve import *
import config
import json

app = Flask(__name__, static_url_path='')


def header_filter(h):
	s = str(h)
	if s == "chr":return "#" + s
	return s

def get_index_list(index_config=None):
	f = open(config.HEADER_INDEX)
	s = f.read()
	header_index = json.loads(s)
	reverse_header = {header_index[k]:k for k in header_index}
	if not index_config:
		index_set = set(header_index.values()).union(config.HEADER_BASIC)
	else:
		index_set = set( [header_index[header_filter(i)] for i in index_config ]).union(config.HEADER_BASIC)
	index_list = sorted(list(index_set))
	return index_list, [reverse_header[i] for i in index_list]

def preprocess_post_header(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if not request.json:
			abort(400)
		r_data = request.get_data()
		j_data = json.loads(r_data)
		#pross j_data
		request.data = {}
		for k in j_data:
			request.data[str(k)] = j_data[k]
		request.data['header_index'], request.data['header'] = get_index_list(request.data.get('annotation_headers', None))
		return f(*args, **kwargs)
	return decorated_function

@app.route('/api/download/<chrsm>', methods=['GET'])
def send_origin_file(chrsm):
	chrsm = int(chrsm)
	return send_from_directory('data', "chr%d.tsv.vcf.sorted.gz" % chrsm, as_attachment=True)

@app.route('/api/origin', methods=['GET'])
def api_origin():
	link_list = [config.HOST + "/download/" + str(i) for i in range(1,23)]
	res = {'data':link_list,
		'format': 'links'}
	return jsonify(res)

@app.route('/api', methods=['GET'])
def get_meta():
	res = {'data_description':'CORECT snp annotation data created on 2018/8/10',
		'format':'text' }
	return jsonify(res)

@app.route('/api/region', methods=["POST"])
@preprocess_post_header
def get_region():
	query_args = request.data
	chrom = query_args.get('chrom')
	start = query_args.get('start')
	end = query_args.get('end')
	header_index = query_args.get('header_index')
	chrom = int(chrom.replace("chr",''))
	start, end = int(start), int(end)
	data = region_q(header_index, chrom, start, end)
	res = {'data':data,
		'status':'success',
		'header':request.data['header'] }
        return jsonify(res)

@app.route('/api/variant', methods=["POST"])
@preprocess_post_header
def get_var():
	query_args = request.data
	chrom = query_args.get('chrom')
	pos = query_args.get('pos')
	ref = query_args.get('ref')
	alt = query_args.get('alt')
	header_index = query_args.get('header_index')
	
	chrom = int(chrom.replace("chr",''))
	pos = int(pos)
	if ref and alt : 
		data = var_q(header_index, chrom, pos, ref, alt)
	else: 
		data = []
	res = {'data':data,
		'status':'success',
		'header':request.data['header'] }
        return jsonify(res)


@app.route('/api/gene')
def gene():
	s = request.args.get('symbol')	
	data = []
	if s:
		data = gene_region(s)
	res = {'data':data,
                'status':'success'}
	return jsonify(res)

@app.route('/api/test', methods=['POST'])
@preprocess_post_header
def test():
	print request.data

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
