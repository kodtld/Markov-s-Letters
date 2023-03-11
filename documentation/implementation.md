# Implementation
## General structure
The program's structure is shown below.

```mermaid
classDiagram
  Server/UI-->MarkovChain
  MarkovChain-->Trie
  Trie-->Books
  Trie-->TrieNode

  class TrieNode
    Node: Dict: children
    Node: Boolean: is_sentence
    Node: Int: Frequency
    
  class Trie
    Trie: Node: root
    Trie: insert_books()
    Trie: insert()
    Trie: generate_ngrams(state)
  
  class MarkovChain
    MarkovChain: Trie: trie
    MarkovChain: Int: state
    MarkovChain: Dict: ngrams (trie.generate_ngrams(state))
    MarkovChain: generate_sentence(starting_prompt, max_length)
    MarkovChain: handle_starting_prompt(starting_prompt, degree)
    MarkovChain: greater_or_equal_prompt(starting_prompt, degree)
    MarkovChain: shorter_prompt(starting_prompt)

  class Books
    
  class Server/UI
  ```

## Space and time complexities
To be updated...

## Points of improvement
To be updated...

## Sources/Links
