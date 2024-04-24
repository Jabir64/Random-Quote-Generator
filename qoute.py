import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney"
    ]
    return random.choice(quotes)

# Example usage
quote = get_random_quote()
print("Random Quote:", quote)