import pyshorteners

# Get URL input from the user
url = input("Enter the URL to be shortened: ")

# Create a Shortener object
shortener = pyshorteners.Shortener()

# Shorten the URL
short_url = shortener.tinyurl.short(url)

# Print the shortened URL
print("Shortened URL:", short_url)
