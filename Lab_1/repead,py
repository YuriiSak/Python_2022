#!/usr/bin/env python3

import collections

def count_repeated_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        words = text.split()
        word_count = collections.Counter(words)
        repeated_words = {word: count for word, count in word_count.items() if count > 1}
        print( repeated_words )

file_path = 'text.txt'
count_repeated_words(file_path)
