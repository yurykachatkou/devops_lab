#!/usr/bin/env python
import json
from snapshot import WriteToFile, WriteToJson

if __name__ == "__main__":
    with open('devops_lab/config.json') as json_file:
        data = json.load(json_file)

    if data["Common"]["output"] == "json":
        WriteToJson("devops_lab/data.json", data["Common"]["interval"])

    elif data["Common"]["output"] == "txt":
        WriteToFile("devops_lab/data.txt", data["Common"]["interval"])
