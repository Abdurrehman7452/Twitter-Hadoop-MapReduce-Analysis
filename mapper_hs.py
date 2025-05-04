#!/usr/bin/env python3

import sys

# Mapper function
def mapper():
    for line in sys.stdin:
        hashtag = line.strip()
        if hashtag:
            print(f"{hashtag}\t1")

if __name__ == "__main__":
    mapper()

