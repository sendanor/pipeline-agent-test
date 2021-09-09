#!/usr/bin/python3

import sys
import json

inputString = sys.argv[1]

input = json.loads(inputString)

print(
  '### ' + input["name"] + "\n\n"
  + input["summary"] + "\n"
)
