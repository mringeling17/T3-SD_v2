#!/usr/bin/python
import json

count = 1
output = {}

while count <= 10:
    # Read file
    with open("/home/hduser/data/op/"+str(count)+".txt/part-00000", "r", encoding="utf-8") as f:
        for line in f:
            # separate word from count as an array
            word, reps = line.split("\t", 1)
            t = {count: int(reps)}
            if word not in output:
                output[word] = {}

            output[word].update(t)

    count += 1

with open("/home/hduser/data/output/output.json", "w", encoding="utf-8") as f:
    json.dump(output, f)
