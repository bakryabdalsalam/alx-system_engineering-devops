import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "My Reddit API Client"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        after = data["data"]["after"]
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no matching posts.")
