"""
Performance testing for the Trie class
"""
import time
from services.trie_service import Trie

trie = Trie()
start_time = time.time()
trie.insert_books()
print("Time taken to insert books:", time.time() - start_time)

word = "example"
start_time = time.time()
print("Searching for the word 'example':", trie.search(word))
print("Time taken to search for the word:", time.time() - start_time)

start_time = time.time()
print("Frequency of the word 'example':", trie.frequency_of(word))
print("Time taken to get frequency of the word:", time.time() - start_time)

start_time = time.time()
print("Next words of the word 'example':", trie.next_word(word))
print("Time taken to get next words of the word:", time.time() - start_time)

start_time = time.time()
print("Next word frequencies of the word 'example':", trie.next_word_frequencies(word))
print("Time taken to get next word frequencies of the word:", time.time() - start_time)
