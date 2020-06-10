# Plugin Poetry by Andrea Landaker is licensed CC BY-NC 4.0
# You can use this code for non-commercial use as long as you credit 
# the author, Andrea Landaker.
# See https://creativecommons.org/licenses/by-nc/4.0/legalcode
#
#
# To customize, create your own lists in wordpacks.rpy and tell the word_board to use them below.

label start:
    $ word_board = Board()
    # This list of all wordpacks allows the user to choose which ones they want
    # If you add more, add them here so the user can choose them.

label change_wordpacks:
    $ wordpack_list = []
    $ wordpack_list.append("basic")
    $ wordpack_list.append("family")
    $ wordpack_list.append("baby")
    $ wordpack_list.append("romance")
    $ wordpack_list.append("farm")
    $ wordpack_list.append("separation")
    $ wordpack_list.append("space")
    $ wordpack_list.append("activism")

    $ chosen_wordpacks = ["basic"]
    # Ask the user what wordpacks they would like
    call screen wordpack_select(wordpack_list)
    $ wordpack_list_choice = _return
    python:
        for i,pack in enumerate(wordpack_list_choice):
            wordpack_list_choice[i] = pack + "_words"
        list_as_string = ",".join(wordpack_list_choice)

        # Create a board with the wordpacks they've chosen
        #word_board = eval("Board(" + list_as_string + ")")
        eval("word_board.set_wordpack(" + list_as_string + ")")


label make_poem:
    $ word_board.generate_display_words()
    call screen plugin_poetry(word_board)
    call screen poetry_display(word_board)
    return
