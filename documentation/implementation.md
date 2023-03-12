# Implementation
## General structure
The program's structure is shown below.

```mermaid
classDiagram
  Server-->Template
  Server-->MarkovChain
  MarkovChain-->Trie
  Trie-->Books
  Trie-->TrieNode

  class TrieNode
    TrieNode: Dict children
    TrieNode: Boolean is_sentence
    TrieNode: Int Frequency
    
  class Trie
    Trie: TrieNode root
    Trie: insert_books()
    Trie: insert(sentence)
    Trie: generate_ngrams(state)
  
  class MarkovChain
    MarkovChain: Trie trie
    MarkovChain: Int state
    MarkovChain: Dict ngrams
    MarkovChain: generate_sentence(starting_prompt, max_length)
    MarkovChain: handle_starting_prompt(starting_prompt, degree)
    MarkovChain: greater_or_equal_prompt(starting_prompt, degree)
    MarkovChain: shorter_prompt(starting_prompt)

  class Books

  class Server
    Server: UI
    Server: index(starting_prompt, state)
    Server: call_generate_sentences(markov_chain, starting_prompt)

  class Template
    Template: index.html
  ```

## Space and time complexities
### Trie
The space complexity of the trie is O(amount of words * average word length * N) where N is the number of sentences in the trie.
#### Insert
Since on average the Trie needs to be travesed N length when inserting a sentence, the time complexity of insert is **O(N)**, where N = length of inserted sentence. <br>
The space complexity of insert is also O(N), where N = length of sentence, since in the worst case N nodes need to be added to trie.
#### Generate Ngrams

### Markov Chain

## Points of improvement
To be updated...

## Sources/Links
