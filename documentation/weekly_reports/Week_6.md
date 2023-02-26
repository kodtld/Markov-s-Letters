# Week 6
### Time spent: 11 hours

## This week
I revamped the generation of senteces completely. Instead of bigrams, my program generates Ngrams depending on the N that user gives as a state. The generation can now be done on any degree of Markov, but on the user side I've limited it to 5 degrees of Markov. I also made the project into an executable, so that it can be easily accessed on every device. I also wrote some new performance and unittests for the revamped functions.

## Challenges
This week was one of the most challengin so far. I spent a large portion of my time to compress the generation of sentences into a one method that allows for different length of prompts to be inputted for any degree of Markov. I also struggled with how I'm going to get the program to work on every system, since our facility machines Cubli 22 gave me problems with poetry.

## Next week
Next week I'll finish up the documentation, and make minor changes to the generator, so that sentences can end before "max_length", if the current word is a word that ends a sentence.
Some minor reformatting and finishing touches.
