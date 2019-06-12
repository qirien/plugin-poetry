# Plugin Poetry by Andrea Landaker is licensed CC-BY 4.0
# You can use this code as long as you credit Andrea Landaker.
# See http://creativecommons.org/licenses/by/4.0/
#
#
# To customize, create your own lists in poetry.rpy and tell the word_board to use them below.

label start:
    scene stars with fade


    # Here you set what Wordpacks you want to use for this session.
    # You can change this if you create other Wordpacks
    $ word_board = Board(basic_words, family_words, farm_words)

label make_poem:
    $ word_board.generate_display_words()
    call screen plugin_poetry(word_board)
    call screen poetry_display(word_board)
    return
