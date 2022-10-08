from argparse import ArgumentParser
from embedder import Embedder

parser = ArgumentParser(description='Process text')
parser.add_argument('--max_length', type=int)

args = parser.parse_args()

embed = Embedder(max_length=args.max_length)
while True:
    text = input()
    outputs = embed.get_embedding([text])
    print(outputs)
