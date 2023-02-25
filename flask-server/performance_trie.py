"""
Performance testing for the Trie class
"""
import time
from services.trie_service import Trie
print("------------------------------------------------------------------------------------------------------------------------------")
print("Performance of the trie_service")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to insert books and generate N_grams with N = 1:")
total_time = 0
for i in range(10):
    start_time = time.time()
    trie = Trie(1)
    trie.insert_books()
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to insert books and generate N_grams with N = 2:")
total_time = 0
for i in range(10):
    start_time = time.time()
    trie = Trie(2)
    trie.insert_books()
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to insert books and generate N_grams with N = 3:")
total_time = 0
for i in range(10):
    start_time = time.time()
    trie = Trie(3)
    trie.insert_books()
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
trie = Trie(2)
word = "example"

print("    Time taken to search for a word:")

total_time = 0
for i in range(10):
    start_time = time.time()
    trie.search(word)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    trie.search(word)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    trie.search(word)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to get frequency of a word:")

total_time = 0
for i in range(10):
    start_time = time.time()
    trie.frequency_of(word)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    trie.frequency_of(word)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    trie.frequency_of(word)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to get the next words of a word:")

total_time = 0
for i in range(10):
    start_time = time.time()
    trie.next_word(word)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    trie.next_word(word)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    trie.next_word(word)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to get the next word frequencies for a word:")

total_time = 0
for i in range(10):
    start_time = time.time()
    trie.next_word_frequencies(word)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    trie.next_word_frequencies(word)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    trie.next_word_frequencies(word)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")
print("------------------------------------------------------------------------------------------------------------------------------")
