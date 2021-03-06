import random
import sys

illegalopcode = [      0x02, 0x03, 0x04, 0x07,             0x0b, 0x0c,       0x0f,
                       0x12, 0x13, 0x14, 0x17,       0x1a, 0x1b, 0x1c,       0x1f,
                       0x22, 0x23,       0x27,             0x2b,             0x2f,
                       0x32, 0x33, 0x34, 0x37,       0x3a, 0x3b, 0x3c,       0x3f,
                       0x42, 0x43, 0x44, 0x47,             0x4b,             0x4f,
                       0x52, 0x53, 0x54, 0x57,       0x5a, 0x5b, 0x5c,       0x5f,
                       0x62, 0x63, 0x64, 0x67,             0x6b,             0x6f,
                       0x72, 0x73, 0x74, 0x77,       0x7a, 0x7b, 0x7c,       0x7f,
                 0x80, 0x82, 0x83,       0x87, 0x89,       0x8b,             0x8f,
                       0x92, 0x93,       0x97,             0x9b, 0x9c, 0x9e, 0x9f,
                             0xa3,       0xa7,             0xab,             0xaf,
                       0xb2, 0xb3,       0xb7,             0xbb,             0xbf,
                       0xc2, 0xc3,       0xc7,             0xcb,             0xcf,
                       0xd2, 0xd3, 0xd4, 0xd7,       0xda, 0xdb, 0xdc,       0xdf,
                       0xe2, 0xe3,       0xe7,             0xeb,             0xef,
                       0xf2, 0xf3, 0xf4, 0xf7,       0xfa, 0xfb, 0xfc,       0xff]

ops = []
for i in range(0, 512):
  while True:
    op = random.randint(0, 255)
    if not op in illegalopcode:
      break
  ops += [op]

sys.stdout.buffer.write(bytes(ops))
