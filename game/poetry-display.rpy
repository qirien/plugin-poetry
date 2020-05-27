##
# This is the screen that shows all the poems you've made.
##

# Computer variant

screen poem_display(poem):
    variant "large"
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        use show_poem(poem)

# mobile variant
screen poem_display(poem):
    frame:
        style_prefix "pps"
        xfill True
        yfill True
        xalign 0.5 
        yalign 0.5
        use show_poem(poem)

# Show one poem in the middle, nice and large
screen show_poem(poem):
    key "mousedown_1" action [Screenshot(), Hide("poem_display", fade)]
    # TODO: add tap anywhere to continue
    frame:
        xalign 0.5 
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            $ poem_string = ""
            for i in range(0, len(poem)):
                hbox:
                    xalign 0.5
                    spacing 5
                    for j in range(0, len(poem[i])):
                        textbutton poem[i][j] text_size 40 action [Screenshot(), Hide("poem_display", fade)]

screen poetry_display(board):
    variant "large"
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        background "#000"
        use p_display(board)

# mobile variant
screen poetry_display(board):
    frame:
        style_prefix "pps"
        xfill True
        yfill True
        background "#000"
        use p_display(board)

screen p_display(board):
    frame:
        xpadding 50
        ypadding 50
        yfill True
        hbox:
            xfill True
            vbox:
                spacing 20
                hbox:
                    label "Poems" text_size 50
                hbox:
                    spacing 30
                    vbox:
                        spacing 30
                        for count in range(0, len(board.poems)):
                            hbox:
                                spacing 30
                                yalign 0.5
                                vbox:
                                    xsize 500
                                    spacing 5
                                    for i in range(0, board.MAX_LINES):
                                        hbox:
                                            spacing 5
                                            if (i < len(board.poems[count])):
                                                for j in range(0, len(board.poems[count][i])):
                                                    textbutton board.poems[count][i][j] action Show("poem_display", dissolve, board.poems[count]) tooltip "Show only this poem"
                                textbutton "Share" action TweetPoem(board.poems[count]) text_size 24 tooltip "Share this poem on Twitter" yalign 0.5

            vbox:
                xalign 0.8
                spacing 5
                null height 50
                textbutton "Add New Poem" action Jump("make_poem") sensitive (len(board.poems) < board.MAX_POEMS) tooltip "Add another poem with the same set of words"
                textbutton "Change Wordpacks" action Jump("change_wordpacks") tooltip "Choose different sets of words"
                textbutton "Screenshot" action Screenshot() tooltip "Take a screenshot, saved in this game's directory"
                # TODO: Add a 'share on twitter' button that just makes a tweet with the poem's text in it.
                textbutton "Save" action ShowMenu("save") tooltip "Save Game"
                textbutton "Done" action Confirm("Done with poems?", Return()) tooltip "Done with Poems"
                null height 50

                fixed:
                    xsize 200
                    $ tooltip = GetTooltip()
                    if tooltip:
                        text tooltip italic True

init python:
    def delete_poem(board, poem_number):
        board.poems.remove(board.poems[poem_number])

    DeletePoem = renpy.curry(delete_poem)

    def tweet_poem(poem):
        import webbrowser
        webbrowser.open_new("http://twitter.com/intent/tweet?text=" + encoded_poem(poem) + "&hashtags=PluginPoetry")

    TweetPoem = renpy.curry(tweet_poem)

    # Take a 2d array of a poem and turn it into an encoded string
    # that can go in a URL for sharing.
    def encoded_poem(poem):
        poem_string = ""
        for i in range(0, len(poem)):   
            for j in range(0, len(poem[i])):
                poem_string += poem[i][j]
                poem_string += "%20"
            poem_string += "%0D%0A"
        
        return poem_string

style pd_button_text is button_text:
    size 16
