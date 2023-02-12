# Implementation
## General structure
The project is a flask application that imports and runs commands from the classes **"trie_service"** and **"markov_service"**, which are stored in the **"services"** directory. To initialize the Trie, **"trie_service"** gets 5 novels from **"resources/books"** and inserts them into itself, the insert also generates bigrams of word pairs, to be later used by the **"markov_service"**. **"Trie_service"** contains all functions regarding the Trie and its nodes, searches, frequencies, and followers, etc.
The **"markov_service"** instance is initialized with all the words and bigrams of the **"trie_service"** instance. The **"markov_service"** uses this information and other getter functions of the **"trie_service"** to calculate propabilities and generate/return sentences.

## Performance
To be updated...

## Points of improvement
To be updated...

## Sources
To be updated...
