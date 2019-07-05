import json

f = open('Problem5Input.json', 'r')
data = json.loads(f.read())

for record in data["Records"]:
	print(record["s3"]["bucket"]["arn"])
	
#Output
# arn:aws:s3:::mybucket

