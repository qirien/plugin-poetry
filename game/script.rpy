# Plugin Poetry by Andrea Landaker is licensed CC-BY 4.0
# You can use this code as long as you credit Andrea Landaker.
# See http://creativecommons.org/licenses/by/4.0/
#
# To customize, add or delete words from these lists.

init python:
    basic_nouns = ["plant", "flower", "seed", "blanket", "fire", "word", "light", "hair", "nose", "toe", "breakfast", "sunrise", "you", "she", "family", "joy", "I", "we", "water", "earth", "air", "planet", "space", "face", "milk", "scent", "father", "mother", "sound", "fruit", "baby", "pain", "me"]
    basic_adjectives = ["beautiful", "blue", "gray", "crimson", "soft", "feathery", "tiny", "young", "gentle", "old", "pink", "rosy", "your", "my", "our", "happy", "simple", "slow", "green", "personal", "bright", "clever", "cute", "chubby", "jealous", "next", "tender", "tight", "precious", "orange", "sweet", "this", "sharp"]
    basic_verbs = ["touch", "feel", "know", "soar", "cry", "hold", "grow", "build", "adore", "love", "babble", "smile", "dance", "sing", "cuddle", "nurture", "thank", "help", "frown", "kick", "glow", "cut", "wrench"]
    basic_other = ["in", "on", "after", "before", "for", "of", "and", "the", "-ing", "-ly", "!", "?", "-s", "forever", "every", "from", "oh", "around", "between", "-y"]
    basic_words = Wordpack()
    basic_words.add_words(basic_nouns, basic_adjectives, basic_verbs, basic_other)

    MAX_LINES = 5
    MAX_POEMS = 5

    NOUN_COLUMNS = 3
    ADJECTIVE_COLUMNS = 3
    VERB_COLUMNS = 2
    OTHER_COLUMNS = 2
    MAX_ROWS = 10
    nouns = list(basic_nouns)
    adjectives = list(basic_adjectives)
    verbs = list(basic_verbs)
    other = list(basic_other)

    display_words = Wordpack()
    display_words.add_wordpacks(basic_words)

init python:
    # If we have more words in a list than will fit nicely on the screen,
    # we take a random sample from that list to use.
    # of words selected will fit on the screen. Then we sort in ABC order.
    def shuffle_word_lists():
        import random
        global nouns, adjectives, verbs, other
        if (len(NOUNS) > (NOUN_COLUMNS * MAX_ROWS)):
            nouns = random.sample(NOUNS, NOUN_COLUMNS * MAX_ROWS)
        nouns.sort()
        if (len(ADJECTIVES) > (ADJECTIVE_COLUMNS * MAX_ROWS)):
            adjectives = random.sample(ADJECTIVES, ADJECTIVE_COLUMNS * MAX_ROWS)
        adjectives.sort()
        if (len(VERBS) > (VERB_COLUMNS * MAX_ROWS)):
            verbs = random.sample(VERBS, VERB_COLUMNS * MAX_ROWS)
        verbs.sort()
        if (len(OTHER) > (OTHER_COLUMNS * MAX_ROWS)):
            other = random.sample(OTHER, OTHER_COLUMNS * MAX_ROWS)
        other.sort()

        renpy.restart_interaction()
        return

    ShuffleWordLists = renpy.curry(shuffle_word_lists)

label start:
    scene stars
    $ poems = []

label make_poem:
    $ shuffle_word_lists()
    $ poem = [[]]
    $ current_line = 0
    call screen plugin_poetry()
    $ poems.append(poem)

    call screen poetry_display()

    return
