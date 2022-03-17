import json

with open('output.txt', 'w') as output_file:
    with open('test.jsonl') as data_file:
        for line in data_file:
            obj = json.loads(line)
            output_file.write(obj["text"] + "\n\n")

