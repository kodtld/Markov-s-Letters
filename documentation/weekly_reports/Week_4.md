# Week 4
### Time spent: 9 hours

## This week
This week I implemented the two-state generation of sentences. At the moment the generation only works without a starting prompt and selects a random bigram to start from. I also worked a bit on the flask side of things and got a running application. The application in its current state only works for the one-state sentences, but "under the hood", it's also possible to generate two-state sentences. Also unnittests for Markovs chain, and some initial performance tests for the Trie.

## Challenges
By far my biggest challenge was to deepen the generation from one-step to two-step. This included storing all the propability bigrams for pairs of words and using them to generate sentences that sound more realistic compared to one-state generations.

## Next week
Next week I'll make the final state option which allows for more than two-state generation of sentences.
I'll also go deeper into the performance testing.
Also I'll make the application usable with all of the current functionality
