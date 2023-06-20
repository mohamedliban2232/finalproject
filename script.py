import re
from collections import Counter

def filter_tweet(tweet):
    # Add your desired filters here
    filtered_tweet = tweet.lower()  # Convert to lowercase
    filtered_tweet = re.sub(r'http\S+', '', filtered_tweet)  # Remove URLs
    filtered_tweet = re.sub(r'@\S+', '', filtered_tweet)  # Remove mentions
    filtered_tweet = re.sub(r'#\S+', '', filtered_tweet)  # Remove hashtags
    return filtered_tweet.strip()

def count_emojis(tweet):
    # Unicode ranges for emojis
    emoji_ranges = [
        (0x1F600, 0x1F99F),  # Emoticons
        (0x1F300, 0x1F5FF),  # Miscellaneous symbols and pictographs
        (0x1F680, 0x1F6FF),  # Transport and map symbols
        (0x2600, 0x26FF),    # Miscellaneous symbols
        (0x2700, 0x27BF),    # Dingbats
        (0xFE00, 0xFE0F)     # Variation Selectors
    ]
    emojis = []
    for start, end in emoji_ranges:
        for codepoint in range(start, end + 1):
            emojis.append(chr(codepoint))
    emoji_pattern = '|'.join(emojis)
    emojis_found = re.findall(emoji_pattern, tweet)
    return Counter(emojis_found)

def process_tweets(file_path):
    tweets = set()  # Set to store unique tweets
    emoji_counts = Counter()  # Counter to store emoji counts

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = filter_tweet(line)
            if tweet not in tweets:
                tweets.add(tweet)
                emoji_counts.update(count_emojis(tweet))

    return emoji_counts

# Usage example
file_path = 'verkiezingen2021.txt'
matrix = process_tweets(file_path)

# Print the matrix
total_emojis = sum(matrix.values())
print(f"Matrix:")
print(f"{'Emoji':<8} {'Count':<8} {'Emoji':<8} {'Count':<8} {'Emoji':<8} {'Count':<8} {'Emoji':<8} {'Count':<8} {'Emoji':<8} {'Count':<8} {'Emoji':<8} {'Count':<8} {'Emoji':<8} {'Count':<8} {'Emoji':<8} {'Count':<8}")
print("-" * 100)
row_count = 0
for emoji, count in matrix.most_common():
    if row_count % 9 == 0:
        print()
    print(f"{emoji:<8} {count:<8}", end=' ')
    row_count += 1
print("\n" + "-" * 100)
print(f"Total Emojis: {total_emojis}")
