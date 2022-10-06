# madlib

A MadLibs game created with Python

## Description

I made a Mad Libs game using Python. Users can opt to enter words to complete a story or generate stories that will have random words added automatically. Option one will show a relationship story that requires manual input.
Option two will show a computer-generated version of the same story.

Option three will deliver a career decision story where users input words, and option four shows the computer-generated version. Option five lets users exit the game.

## Design and Implementation Main Structure

The main structure is a while loop that calls the menu function and an if statement which checks the menu choice. There’s a game_pkg folder that contains a main_functions.py file that houses the word bank, story tuples, and functions.

### Options One and Three

Users who select the first or third options will be asked to input some nouns, names, adjectives, adverbs, numbers, and a few other words one at a time.
They will then see the story that includes the words they entered. Next, they will be presented with the menu again.

Options one and three use the input function and append method to add words to lists. Bracket notation adds those words to the story. The print function is used to show the finished story to the user.

I initially used the input function and variables. Variables worked wonderfully, but I used lists and bracket notation to show more of the skills I learned.
The lists work just as well as the variables, so making things more complicated didn’t cause issues. I used variables for parts of the stories in italics.

### Options Two and Four

Options two and four are computer-generated versions of the stories used in options one and three. The two stories are concatenated strings inside of a tuple.

A word bank is stored in a dictionary where the keys are the word types, and the values are random words of each type.
The random_word function has the word bank keys and a local copy of the word bank as parameters. It randomizes the words and removes them from the local copy of the word bank as they are used.

The format method is used in the new_story2 and new_story4 functions to add the random words to the story tuples.

I had trouble getting the game to work as one file. I added the word bank and the functions above the while loop but still had issues. After I moved the functions and word bank to a different file and imported them, the game worked for all options.

## Best Features and Shortcomings

The best feature of the game is using bracket notation to add words to the story for options one and three. Using bracket notation allows me to add specific terms to different story parts.

I didn’t try to add specific words to different areas in the computer-generated stories since they use randomization. I slightly changed the stories for options two and four from the options one and three versions since I couldn’t reuse specific inputted words.

For example, the career drama in option three refers to the same city in different areas and uses the main character’s name multiple times. I updated the computer-generated version with pronouns because it would be confusing if random names showed in those places.
