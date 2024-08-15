import msgpack
import json
import argparse

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--map_path', type=str, required=True)
  
  return parser.parse_args()

def main():
  args = parse_args()
  
  with open(args.map_path, 'rb') as f:
    unpackers = msgpack.Unpacker(f, raw=False)
    for unpacker in unpackers:
      print(unpacker)
      
      
if __name__ == '__main__':
  main()
