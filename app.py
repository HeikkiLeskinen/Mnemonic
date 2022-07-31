import json
import sys

def dominic_system(first, second):
    with open('./data/dominic_system.json') as d:
        data = json.load(d)
        subject = [value["subject"] for value in data if value["number"] == int(first)][0] 
        verb = [value["verb"] for value in data if value["number"] == int(second)][0] 
        print("{} {}".format(subject, verb))

if len(sys.argv) != 2:
    print("Usage: python {} <number>".format(sys.argv[0]))
    exit(1)    
    
number = sys.argv[1]
chunk_size = 4

for item in [number[i:i+chunk_size] for i in range(0, len(number), chunk_size)]:
    if len(item) == 4:
        dominic_system(item[:2], item[2:])
 
