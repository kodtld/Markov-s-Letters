import time
from services.trie_service import Trie
from services.markov_service import MarkovChain

trie = Trie()
trie.insert_books()

markov_chain = MarkovChain(trie)
print("------------------------------------------------------------------------------------------------------------------------------")
print("Performance of the markov_service")
print("------------------------------------------------------------------------------------------------------------------------------")

word = "example"
print("    Time taken to generate one-state sentence with no starting word and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=None, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=None, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=None, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate one-state sentence with a starting word and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate two-state sentence with no starting bigram and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_two_sentence(starting_word=None, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_two_sentence(starting_word=None, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_two_sentence(starting_word=None, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate two-state sentence with a starting bigram and max length of 10:")
bigram = "example that"
total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_two_sentence(starting_word=bigram, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_two_sentence(starting_word=bigram, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_two_sentence(starting_word=bigram, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")