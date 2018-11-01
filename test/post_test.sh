python gen_json_request.py chrom=chr2 pos=100008 ref=T alt=A config.json
#cat tmp.json
curl -H "Content-Type: application/json" --data @tmp.json http://localhost:5000/api/variant|json_pp
rm tmp.json

python gen_json_request.py chrom=chr2 start=100007 end=101000 config.json
curl -H "Content-Type: application/json" --data @tmp.json http://localhost:5000/api/region|json_pp
rm tmp.json

python gen_json_request.py chrom=chr2 start=100007 end=101000 annovar.config
cat tmp.json|json_pp
curl -H "Content-Type: application/json" --data @tmp.json http://localhost:5000/api/region|json_pp
rm tmp.json

python gen_json_request.py chrom=chr2 pos=100008 ref=T alt=A annovar.config
cat tmp.json|json_pp
curl -H "Content-Type: application/json" --data @tmp.json http://localhost:5000/api/variant|json_pp
rm tmp.json
