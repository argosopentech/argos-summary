import argparse


parser = argparse.ArgumentParser(description="Generates summarization data")
parser.add_argument(
    "datafile",
    help="A file with text data",
)
args = parser.parse_args()

with open(args.datafile, 'r') as datafile:
    data = datafile.read()
    paragraphs = data.split("\n\n")
    sourcelines = list()
    targetlines = list()
    for paragraph in paragraphs:
        first_period_index = paragraph.find(".")
        if paragraph.count(".") < 4:
            continue
        if len(paragraph) < 100:
            continue
        if len(paragraph) > 5000:
            continue
        if first_period_index < 1:
            continue
        if len(paragraph) - first_period_index < 1:
            continue
        first_sentence = paragraph[:first_period_index + 1]
        remaining_text = paragraph[first_period_index + 1:]
        for line in first_sentence.split("\n"):
            if line.find(".") >= 0:
                first_sentence = line
        if len(first_sentence) < 15:
            continue
        first_sentence = first_sentence.strip()
        remaining_text = remaining_text.strip()
        sourcelines.append(first_sentence)
        targetlines.append(remaining_text)
        print(paragraph)
        print("\n\n")
        print(first_sentence)
        print("\n\n")
        print(remaining_text)
        print("\n\n")
        print("-" * 40)
        print("\n\n")

