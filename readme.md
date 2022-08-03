# Koan
A Twitter bot that mixes up sentences from a library of plain text files, integrates them into a custom prompt for OpenAI and tweets it.

Wombo AI image generation is a work in progress.

# Installation
1. `pip install tweepy`
1. `pip install openai`

# How To Use
1. Enter your Twitter and OpenAI credentials in config.json.
2. Test koan.py by running Python 3, importing it as `import koan` and calling `koan.get_koans(amount=1, keywords=[], sentences_per_book=50)`.
3. Run tweet.py to send a tweet using OpenAI and the koan.

# Library Resources
Project Gutenberg has a large collection of free plain text books.
