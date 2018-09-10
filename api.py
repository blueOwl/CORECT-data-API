from flask import Flask, request, send_from_directory, jsonify
from data_retrieve import *

HOST = "http://206.189.218.218:5000/api"
app = Flask(__name__, static_url_path='')
@app.route('/api/download/<chrsm>')
def send_origin_file(chrsm):
	chrsm = int(chrsm)
	return send_from_directory('data', "chr%d.tsv.vcf.sorted.gz" % chrsm, as_attachment=True)

@app.route('/api/origin')
def api_origin():
	link_list = [HOST + "/download/" + str(i) for i in range(1,23)]
	res = {'data':link_list,
		'format': 'links'}
	return jsonify(res)

@app.route('/api')
def get_meta():
	res = {'data':'meta info',
		'format':'text' }
	return jsonify(res)

@app.route('/api/region')
def get_region():
	print request.args
	chrom = request.args.get('chrom')
	start = request.args.get('start')
	end = request.args.get('end')
	chrom = int(chrom.replace("chr",''))
	start, end = int(start), int(end)
	data = region_q(chrom, start, end)
	res = {'data':data,
                'format': 'vcf'}
        return jsonify(res)

@app.route('/api/variant')
def get_var():
	chrom = request.args.get('chrom')
	pos = request.args.get('pos')
	ref = request.args.get('ref')
	alt = request.args.get('alt')
	
	chrom = int(chrom.replace("chr",''))
	pos = int(pos)
	data = var_q(chrom, pos, ref, alt)
	res = {'data':data,
                'format': 'vcf'}
        return jsonify(res)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
