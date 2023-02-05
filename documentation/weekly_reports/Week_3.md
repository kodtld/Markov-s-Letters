# Week 3
### Time spent: 11 hours

## This week
This week I finally reached a working minimum viable product. The program is able to do one-step sentence generations.
Most of my time went towards adding functionality to the Trie and getting the right outputs to pass for my Markov Chain.
At the moment the program generates sentences in a one step process, only taking into consideration what words can come after the last word in current sentece.

## Challenges
My largest challenge was to find exactly what I should pass to the Markov Chain from the Trie, and how to do that.
Also writing the getter function that returns every word with its frequency and its followers took some effort.

## Next week
Next week I'll write tests for the Markov Chain generator. I also plan on trying to deepen the state of the generation 
from one-state markov to two- and three-step markovs. I think getting the trie to return following words for a sequence will be my biggest challenge.
Maybe I'll work a bit on the front-end if I have spare time.
