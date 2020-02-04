cat filename.json | python - c 'import sys, yaml, json; j=json.loads(sys.stdin.read()); print yaml.safe_dump(j)' > filename.yaml
