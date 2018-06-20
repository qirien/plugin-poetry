# Plugin Poetry by Andrea Landaker is licensed CC-BY 4.0
# You can use this code as long as you credit Andrea Landaker.
# See http://creativecommons.org/licenses/by/4.0/
#
# To customize, add or delete words from these lists.

init python:
    basic_nouns = ["word", "breakfast", "sunrise", "you", "she", "joy", "I", "we",  "scent", "sound", "me", "pain", "wonder"]
    basic_adjectives = ["beautiful", "blue", "gray", "crimson", "soft", "feathery",  "pink", "your", "my", "our", "orange", "this"]
    basic_verbs = ["jump", "know", "soar", "smile", "dance", "sing", "kick", "glow", "cut", "wrench"]
    basic_other = ["in", "on", "after", "before", "for", "of", "and", "the", "-ing", "-ly", "!", "?", "-s", "every", "from", "around", "between", "-y"]
    basic_words = Wordpack()
    basic_words.add_words(basic_nouns, basic_adjectives, basic_verbs, basic_other)

    family_nouns = ["blanket", "hair", "nose", "toe", "family", "joy", "face", "milk", "scent", "father", "mother", "baby"]
    family_adjectives = ["tiny", "young", "gentle", "old", "rosy", "happy", "personal", "bright", "clever", "cute", "chubby", "jealous", "tender", "tight", "precious", "sweet"]
    family_verbs = ["touch", "feel", "cry", "hold", "grow", "build", "adore", "love", "babble", "cuddle", "nurture", "thank", "help", "frown"]
    family_other = ["forever", "oh"]
    family_words = Wordpack()
    family_words.add_words(family_nouns, family_adjectives, family_verbs, family_other)

    farm_nouns = ["plant", "flower", "seed", "fire", "light", "water", "earth", "air", "planet", "space", "fruit", "harvest"]
    farm_adjectives = ["simple", "slow", "green", "personal", "sharp", "alive", "dead"]
    farm_verbs = ["soar", "grow", "build", "help", "cut", "wrench"]
    farm_other = ["yum"]
    farm_words = Wordpack()
    farm_words.add_words(farm_nouns, farm_adjectives, farm_verbs, farm_other)

    MAX_LINES = 5
    MAX_POEMS = 5

    NOUN_COLUMNS = 3
    ADJECTIVE_COLUMNS = 3
    VERB_COLUMNS = 2
    OTHER_COLUMNS = 2

    MAX_ROWS = 10
    MAX_NOUNS = NOUN_COLUMNS * MAX_ROWS
    MAX_VERBS = VERB_COLUMNS * MAX_ROWS
    MAX_ADJECTIVES = ADJECTIVE_COLUMNS * MAX_ROWS
    MAX_OTHER = OTHER_COLUMNS * MAX_ROWS

    # Reselect words for lists
    # TODO: Doesn't work. Maybe we need to pass two lists;
    # a master list and a display list? Somehow
    def shuffle_word_lists():
        display_words = Wordpack()
        display_words.add_wordpacks(basic_words, family_words, farm_words)
        display_words.trim_to_size([MAX_NOUNS, MAX_ADJECTIVES, MAX_VERBS, MAX_OTHER])
        renpy.restart_interaction()
        return

    ShuffleWordLists = renpy.curry(shuffle_word_lists)

label start:
    scene stars
    $ poems = []

label make_poem:
    $ poem = [[]]
    $ current_line = 0
    $ display_words = Wordpack()
    $ display_words.add_wordpacks(basic_words, family_words, farm_words)
    $ display_words.trim_to_size([MAX_NOUNS, MAX_ADJECTIVES, MAX_VERBS, MAX_OTHER])
    call screen plugin_poetry(display_words)
    $ poems.append(poem)

    call screen poetry_display()

    return
