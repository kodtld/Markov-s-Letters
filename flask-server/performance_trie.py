"""
Performance testing for the Trie class
"""
import time
from services.trie_service import Trie
print("-----------------------------------------------------")
print("Performance of the trie_service")
print("-----------------------------------------------------")
trie = Trie()
start_time = time.time()
trie.insert_books()
print("    Time taken to insert books:", time.time() - start_time)
print("-----------------------------------------------------")
word = "example"
start_time = time.time()
trie.search(word)
print("    Time taken to search for the word:", time.time() - start_time)
print("-----------------------------------------------------")
start_time = time.time()
trie.frequency_of(word)
print("    Time taken to get frequency of the word:", time.time() - start_time)
print("-----------------------------------------------------")
start_time = time.time()
trie.next_word(word)
print("    Time taken to get next words of the word:", time.time() - start_time)
print("-----------------------------------------------------")
start_time = time.time()
trie.next_word_frequencies(word)
print("    Time taken to get next word frequencies of the word:", time.time() - start_time)
print("-----------------------------------------------------")
