#!/usr/bin/env pytho
import json
from snapshot.snapshot import WriteToFile, WriteToJson
from snapshot import config

if __name__ == "__main__":
    filetype = config.config['Common']['output']
    interval = config.config['Common']['interval']

    if filetype == "json":
        WriteToJson("data.json", interval)

    elif filetype == "txt":
        WriteToFile("data.txt", interval)

