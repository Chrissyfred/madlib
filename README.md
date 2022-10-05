# madlib
A MadLibs game created with Python

Introduction

I made a Mad Libs game using Python. Users can opt to enter words to complete a story or generate stories that will have random words added automatically. Option one will show a relationship story that requires manual input.
Option two will show a computer-generated version of the same story.

Option three will deliver a career decision story where users input words, and option four shows the computer-generated version. Option five lets users exit the game.

Design and Implementation Main Structure

The main structure is a while loop that calls the menu function and an if statement which checks the menu choice. There’s a game_pkg folder that contains a main_functions.py file that houses the word bank, story tuples, and functions.

Options One and Three
Users who select the first or third options will be asked to input some nouns, names, adjectives, adverbs, numbers, and a few other words one at a time.
They will then see the story that includes the words they entered. Next, they will be presented with the menu again.

Options one and three use the input function and append method to add words to lists. Bracket notation adds those words to the story. The print function is used to show the finished story to the user.
I initially used the input function and variables. Variables worked wonderfully, but I used lists and bracket notation to show more of the skills I learned.
The lists work just as well as the variables, so making things more complicated didn’t cause issues. I used variables for parts of the stories in italics.

Best Features and Shortcomings

The best feature of the game is using bracket notation to add words to the story for options one and three. Using bracket notation allows me to add specific terms to different story parts.

I didn’t try to add specific words to different areas in the computer-generated stories since they use randomization. I slightly changed the stories for options two and four from the options one and three versions since I couldn’t reuse specific inputted words.

For example, the career drama in option three refers to the same city in different areas and uses the main character’s name multiple times. I updated the computer-generated version with pronouns because it would be confusing if random names showed in those places.
