# Plugin Poetry by Andrea Landaker is licensed CC-BY 4.0
# You can use this code as long as you credit Andrea Landaker.
# See http://creativecommons.org/licenses/by/4.0/
#
# To customize, add or delete words from these lists.

init python:
    poem = [[""]]
    current_line = 0
    nouns = ["weed", "flower", "seed", "blanket", "knife", "fire", "words", "light", "hair", "nose", "toes", "breakfast", "sunrise", "you", "she", "family", "joy", "I"]
    adjectives = ["beautiful", "blue", "gray", "crimson", "soft", "feathery", "tiny", "young", "gentle", "old", "pink", "rosy", "your", "my", "our", "happy"]
    verbs = ["touch", "feel", "know", "soar", "grieve", "hold", "grow", "build", "adore", "love"]
    other = ["on", "after", "before", "for", "of", "and", "the", "ing", "ly", "!", "?", "s", "forever", "every"]

label start:

    scene stars
    "Welcome to Plugin Poetry...Build your poem and share it."

    # TODO: randomize, alphabetize them, or pick a limited number of them
    #$ random.shuffle(nouns)
    #$ random.shuffle(adjectives)
    #$ random.shuffle(verbs)
    #$ random.shuffle(other)

label make_poem:
    $ poems = []
    $ poem = [[""]]
    $ current_line = 0
    call screen plugin_poetry()
    $ poems.append(poem)

    menu:
        "What would you like to do now?"
        "Make another poem.":
            jump make_poem
        "Read poems made.":
            $ count = 0
            while (count < len(poems)): # for each poem
                "Poem [count]:"
                $ line = 0
                $ poem_str = ""
                while (line < len(poems[count])): # for each line of the poem
                    $ word = 0
                    while (word < len(poems[count][line])): # for each word of the poem
                        $ poem_str += poems[count][line][word]
                        $ poem_str += " "
                        $ word += 1
                    $ line += 1
                    $ poem_str += "\n"
                "[poem_str]"
                $ count += 1
            $ pass
        "Quit":
            $ renpy.quit()

    return
