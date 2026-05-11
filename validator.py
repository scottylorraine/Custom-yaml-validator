import sys, json, yaml, urllib.request
from jsonschema import Draft7Validator

url = "https://raw.githubusercontent.com/harness/harness-schema/main/v0/template.json"
schema = json.loads(urllib.request.urlopen(url).read())
data = yaml.safe_load(open(sys.argv[1]))

errors = sorted(Draft7Validator(schema).iter_errors(data), key=lambda e: e.path)

if errors:
    e = errors[0]
    path = ".".join(map(str, e.path)) or "root"
    print(f"invalid: {path}: {e.message}")
    sys.exit(1)

print("valid")
