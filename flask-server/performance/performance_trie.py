"""
Performance testing for the Trie class
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from services.trie_service import Trie
import time

print("------------------------------------------------------------------------------------------------------------------------------")
print("Performance of the trie_service")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to insert books")
total_time = 0
for i in range(10):
    start_time = time.time()
    trie = Trie()
    trie.insert_books()
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to generate N_grams with N = 1:")
total_time = 0
for i in range(10):
    start_time = time.time()
    trie.generate_ngrams(1)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
print("    Time taken to generate N_grams with N = 2:")
total_time = 0
for i in range(10):
    start_time = time.time()
    trie.generate_ngrams(2)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate N_grams with N = 3:")
total_time = 0
for i in range(10):
    start_time = time.time()
    trie.generate_ngrams(3)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")
