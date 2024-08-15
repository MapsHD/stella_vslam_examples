import msgpack

with open('map.map') as f:
  unpackers = msgpack.Unpacker(f, raw=False)
  for unpacker in unpackers:
    print(unpacker)
