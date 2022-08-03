#! /usr/bin/python3
from os import walk
import random
import json
import re

config = json.load(open("/home/chris/dev/koan/config.json"))
library_directory = config["library_directory"]
excluded_words = config["excluded_words"]
sentence_collection = []

def get_books_in_library():
    return next(walk(library_directory), (None, None, []))[2]

def select_random_book():
    books = get_books_in_library()
    return books[random.randrange(0, len(books))]

def collect_sentences(sentences_per_book, keywords):
    global sentence_collection
    keywords = [x.lower() for x in keywords]

    for book in get_books_in_library():
        sentences = []
        sentences_with_keywords = []
        chosen_sentences = []

        # Read all sentences from the book
        with open(f"{library_directory}/{book}") as f:
            sentences += re.findall(r".*?[\.\!\?]+", f.read())

        # Find sentences that include keywords
        if keywords != []:
            for sentence in sentences:
                for word in sentence.split(" "):
                    if word.lower() in keywords:
                        sentences_with_keywords.append(sentence)
                    else:
                        for x in keywords:
                            if x in word.lower():
                                sentences_with_keywords.append(sentence)

        # Add random sentences with keywords to list
        random.shuffle(sentences_with_keywords)
        for sentence in sentences_with_keywords:
            if len(chosen_sentences) < sentences_per_book:
                chosen_sentences.append(sentence)

        # Choose random sentences to fill the rest
        while len(chosen_sentences) < sentences_per_book:
            x = random.randrange(0, len(sentences))
            chosen_sentences.append(sentences[x])

        # Add chosen sentences to collection
        sentence_collection.extend(chosen_sentences)

def get_random_sentence(minimum_words):
    global sentence_collection
    global excluded_words

    while True:
        fail = False
        sentence = sentence_collection[random.randrange(0, len(sentence_collection))]
        if len(sentence.split(' ')) < minimum_words:
            fail = True
        for word in excluded_words: 
            if word in sentence:
                fail = True
        if not fail:
            return sentence

def get_random_sentences(n, minimum_words):
    sentences = []
    for i in range(n):
        sentences.append(get_random_sentence(minimum_words))
    return sentences

def print_sentences(sentences):
    for sentence in sentences:
        print(sentence)

def get_sentence_fragment(sentence, first_half):
    sentence = sentence.split(" ")
    fragment = ""

    if first_half:
        for i in range(0, random.randrange(1, len(sentence))):
            fragment += f"{sentence[i]} "
    else:
        for i in range(random.randrange(1, len(sentence) - 1), len(sentence)):
            fragment += f" {sentence[i]}"
        fragment = fragment[1:]
            
    return fragment

def clean_sentence(sentence):
    sentence = sentence.strip()
    sentence = sentence.replace('\n', '')
    sentence = sentence.replace('“', '')
    sentence = sentence.replace('”', '')
    sentence = sentence.replace('"', '')
    sentence = sentence.replace('_', '')
    sentence = sentence.replace('--', '')
    sentence = sentence.replace('--', '')
    sentence = sentence.replace('--', '')
    sentence = sentence.replace('(', '')
    sentence = sentence.replace(')', '')
    sentence = sentence.replace('  ', ' ')
    sentence = sentence.replace('   ', ' ')
    sentence = sentence.replace('  ', ' ')
    sentence = sentence.replace('—', '')
    sentence = sentence.replace('   ', ' ')
    sentence = sentence.strip()
    sentence = sentence[0].upper() + sentence[1:]
    return sentence

def combine_two_sentences(sentences):
    sentence = f"{get_sentence_fragment(sentences[0], True)}{get_sentence_fragment(sentences[1], False)}"
    sentence = clean_sentence(sentence)
    return sentence

def get_koans(amount=1, keywords=[], sentences_per_book=50):
    collect_sentences(sentences_per_book, keywords)
    koans = []
    for i in range(amount):
        sentences = get_random_sentences(2, 7)
        koans.append(combine_two_sentences(sentences))
    return koans

def get_koan():
    collect_sentences(50)
    sentences = get_random_sentences(2, 7)
    return combine_two_sentences(sentences)
