#!/usr/bin/python3
import random

programming_jokes = [
  "Why don't programmers like nature? It has too many bugs.",
  "Why did the CSS developer go to therapy? To get rid of his margins.",
  "How do you comfort a JavaScript developer? You console them.",
  "Why did the CSS developer leave the restaurant? Because it had no class.",
  "Why did the JavaScript developer go missing? Because he didn't know when to return.",
  "Why did the HTML tag go to the party? Because it wanted to break the line.",
  "Why do JavaScript developers wear glasses? Because they don't C#.",
  "Why don't programmers like to use inline styles? Because they want to be classy.",
  "Why did the CSS selector break up with the HTML element? It found someone more specific.",
  "Why did the CSS developer apply for a job? They wanted to get a position.",
]

random_dad_jokes = [
    "A red and a blue ship have just collided in the Caribbean. Apparently the survivors are marooned.",
    "Why do cows wear bells? Because their horns don't work.",
    "I'll tell you what often gets over looked... garden fences.",
    "I needed a password eight characters long so I picked Snow White and the Seven Dwarfs.",
    "I wanted to be a tailor but I didn't suit the job",
    "What kind of dinosaur loves to sleep? A stega-snore-us.",
    "I'm tired of following my dreams. I'm just going to ask them where they are going and meet up with them later.",
    "what do you call a dog that can do magic tricks? a labracadabrador",
    "What is the leading cause of dry skin? Towels",
    "Dermatologists are always in a hurry. They spend all day making rash decisions.",
    "I won an argument with a weather forecaster once. His logic was cloudy...",

]

print("Random Programming Jokes of the day is:\n", random.choice(programming_jokes))

# Print two jokes at a time
print("Random 2 Dad Jokes of the day is:\n", random.sample(random_dad_jokes, 2))
