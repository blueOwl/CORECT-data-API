python gen_json_request.py chrom=chr2 start=100007 end=101000 default.json
cat tmp.json|json_pp
curl -H "Content-Type: application/json" --data @tmp.json http://localhost:5000/api/region|json_pp
rm tmp.json
