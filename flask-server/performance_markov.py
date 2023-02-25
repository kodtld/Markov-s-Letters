import time
from services.trie_service import Trie
from services.markov_service import MarkovChain

print("------------------------------------------------------------------------------------------------------------------------------")
print("Performance of the markov_service")
print("------------------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------------------")
print("One-state Markov Chain")
print("------------------------------------------------------------------------------------------------------------------------------")

equal_word = "world"
greater_word = "world is"
trie = Trie(1)
trie.insert_books()
markov_chain = MarkovChain(trie)

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

print("    Time taken to generate one-state sentence with a starting word of equal length to degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate one-state sentence with a starting word of greater length do degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------------------")
print("Two-state Markov Chain")
print("------------------------------------------------------------------------------------------------------------------------------")

shorter_word = "world"
equal_word = "world is"
greater_word = "world is round"
trie = Trie(2)
trie.insert_books()
markov_chain = MarkovChain(trie)

print("    Time taken to generate two-state sentence with no starting word and max length of 10:")

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

print("    Time taken to generate two-state sentence with a starting word of shorter length to degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=shorter_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=shorter_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=shorter_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate two-state sentence with a starting word of equal length to degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate two-state sentence with a starting word of greater length do degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------------------")
print("Three-state Markov Chain")
print("------------------------------------------------------------------------------------------------------------------------------")

shorter_word = "world is"
equal_word = "world is round"
greater_word = "world is round so"
trie = Trie(3)
trie.insert_books()
markov_chain = MarkovChain(trie)

print("    Time taken to generate three-state sentence with no starting word and max length of 10:")

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

print("    Time taken to generate three-state sentence with a starting word of shorter length to degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=shorter_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=shorter_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=shorter_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate three-state sentence with a starting word of equal length to degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=equal_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")

print("    Time taken to generate three-state sentence with a starting word of greater length do degree and max length of 10:")

total_time = 0
for i in range(10):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 10
print(f"        Total times of 10 operations: {total_time:.6f} seconds | Average time of 10 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(100):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 100
print(f"        Total times of 100 operations: {total_time:.6f} seconds | Average time of 100 operations: {avg_time:.6f} seconds")

total_time = 0
for i in range(1000):
    start_time = time.time()
    markov_chain.generate_sentence(starting_word=greater_word, max_length=10)
    total_time += time.time() - start_time
avg_time = total_time / 1000
print(f"        Total times of 1000 operations: {total_time:.6f} seconds | Average time of 1000 operations: {avg_time:.6f} seconds")

print("------------------------------------------------------------------------------------------------------------------------------")