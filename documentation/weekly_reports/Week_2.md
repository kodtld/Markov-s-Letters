# Week 2
### Time spent: 12 hours

## This week
I had to change my subject from predicting words to generating sentences.
I implemented the Trie data-structure and in its current state it's initialized with 5 novels.
The trie has operations for searching words and their frequensy, and can output a dictionary of possible words after given word.
I also wrote unittests for said Trie, figured my CI pipeline, and implemented Pylint into my project.

## Challenges
I had multiple challenges with the Trie, firstly, inserting the books into the Trie took a bit of work.
After the insertion I had troubles with specifying when a word ends and where a sentence ends.
Also getting the right frequency took a bit of my time.

## Next week
Next week I'll add a stripping method that removes special characters from inserted sentences.
I'll add a possibility to show possible next words for a sequence of given words.
Also start the work on the Markov's chain itself.
