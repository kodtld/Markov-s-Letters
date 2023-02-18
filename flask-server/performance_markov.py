import time
from services.trie_service import Trie
from services.markov_service import MarkovChain

trie = Trie()
trie.insert_books()

markov_chain = MarkovChain(trie)

num_trials = 100
total_time = 0
for i in range(num_trials):
    start_time = time.time()
    generated_sentence = markov_chain.generate_sentence(starting_word=None, max_length=20)
    total_time += time.time() - start_time
avg_time = total_time / num_trials
print(f"Average time taken to generate sentence: {avg_time:.6f} seconds")
