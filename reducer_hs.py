#!/usr/bin/env python3

import sys
from collections import defaultdict

def reducer():
    hashtag_counts = defaultdict(int)

    # Read input from stdin
    for line in sys.stdin:
        line = line.strip()
        if line:
            hashtag, count = line.split('\t', 1)
            try:
                count = int(count)
            except ValueError:
                continue
            hashtag_counts[hashtag] += count

    # Sort hashtags by count in descending order
    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)

    # Write results to a file
    with open('hashtagpopularity.txt', 'w') as file:
        # Write heading
        file.write("HASHTAG\tCOUNT\n")
        
        # Write top 15 hashtags
        for hashtag, count in sorted_hashtags[:15]:
            file.write(f"{hashtag}\t{count}\n")

    # Print the top 15 hashtags to stdout
    print("Top 15 Most Popular Hashtags:")
    print("HASHTAG\tCOUNT")
    for hashtag, count in sorted_hashtags[:15]:
        print(f"{hashtag}\t{count}")

if __name__ == "__main__":
    reducer()

