#!/usr/bin/env python3
import sys
import json

def mapper():
    for line in sys.stdin:
        try:
            data = json.loads(line)
            user_name = data.get('user_name')
            user_followers = int(data.get('user_followers', 0))
            user_favourites = int(data.get('user_favourites', 0))
            user_verified = data.get('user_verified', False)
            
            # Assigning a weight to verified status
            verified_score = 1 if user_verified else 0
            
            # Emit user name and combined influence score components
            print(f"{user_name}\t{user_followers}\t{user_favourites}\t{verified_score}")
        except json.JSONDecodeError:
            continue

if __name__ == "__main__":
    mapper()

