#!/usr/bin/env python3
import sys

def reducer():
    current_user = None
    total_followers = 0
    total_favourites = 0
    is_verified = 0

    # Composite influence score weights
    follower_weight = 1
    favourite_weight = 0.25
    verified_weight = 100  # Heavier weight for verification

    # Dictionary to hold aggregated data for each user
    user_data = {}

    for line in sys.stdin:
        line = line.strip()
        user_name, user_followers, user_favourites, verified_score = line.split("\t")

        # Convert strings to appropriate types
        user_followers = int(user_followers)
        user_favourites = int(user_favourites)
        verified_score = int(verified_score)

        # If the user already exists in the dictionary, update their data
        if user_name in user_data:
            user_data[user_name]['followers'] += user_followers
            user_data[user_name]['favourites'] += user_favourites
            user_data[user_name]['verified'] = max(user_data[user_name]['verified'], verified_score)
        else:
            # Initialize the user's data if they don't exist in the dictionary
            user_data[user_name] = {
                'followers': user_followers,
                'favourites': user_favourites,
                'verified': verified_score
            }

    # Calculate influence scores and store them in a list
    user_influence_scores = []
    for user_name, data in user_data.items():
        influence_score = ((data['followers'] * follower_weight +
                            data['favourites'] * favourite_weight +
                            data['verified'] * verified_weight) / 100)
        user_influence_scores.append((influence_score, user_name))

    # Sort users by influence score in descending order
    user_influence_scores.sort(reverse=True, key=lambda x: x[0])

    # Print top 25 influential users
    print("Top 25 influential users on X")
    print("USER\t\t\t\tUSER SCORE")
    for score, user in user_influence_scores[:25]:
        print(f"{user}\t\t\t\t{score:.1f}")

if __name__ == "__main__":
    reducer()

