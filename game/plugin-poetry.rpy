screen plugin_poetry:
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        background "images/stars.jpg"
        frame:
            xpadding 50
            yfill True
            background "#aaaaaa"
            vbox: # Poem, then words
                vbox: # Title, then poem
                    xfill True
                    spacing 5
                    label "New Poem" text_size 50 xalign 0.5
                    hbox:
                        spacing 20
                        xalign 0.5
                        textbutton "Reset" action Confirm("Delete this poem?", Reset(True))
                        textbutton "Done" action Return()
                    hbox: # Poem lines
                        spacing 2
                        vbox:
                            yalign 0.5
                            spacing 10
                            textbutton "▲" action PreviousLine() sensitive(current_line>1) size_group "nav_buttons"
                            textbutton "×" action Confirm("Delete line?", Reset(False)) size_group "nav_buttons"
                            textbutton "▼" action NextLine() sensitive(current_line< (MAX_LINES-1)) size_group "nav_buttons"
                        vbox:
                            for i in range(0, MAX_LINES):
                                hbox:
                                    spacing 2
                                    null height 35
                                    if (i < len(poem)):
                                        if (i == current_line):
                                            label "→"
                                        for j in range(0, len(poem[i])):
                                            textbutton poem[i][j] action DeleteWord(j)
                hbox:
                    spacing 20
                    xfill True
                    vbox:
                        yalign 0.5
                        spacing 10
                        textbutton "+" action renpy.curried_invoke_in_new_context(textinput) size_group "nav_buttons"
                        textbutton "↔" action ShuffleWordLists() size_group "nav_buttons"
                    vbox:
                        label "Nouns"
                        vpgrid:
                            cols NOUN_COLUMNS
                            for i in range(0, len(nouns)):
                                textbutton nouns[i] action AddWord(nouns[i]) size_group "word"

                    vbox:
                        label "Adjectives"
                        vpgrid:
                            cols ADJECTIVE_COLUMNS
                            for i in range(0, len(adjectives)):
                                textbutton adjectives[i] action AddWord(adjectives[i]) size_group "word"

                    vbox:
                        label "Verbs"
                        vpgrid:
                            cols VERB_COLUMNS
                            for i in range(0, len(verbs)):
                                textbutton verbs[i] action AddWord(verbs[i]) size_group "word"

                    vbox:
                        label "Other"
                        vpgrid:
                            cols OTHER_COLUMNS
                            for i in range(0, len(other)):
                                textbutton other[i] action AddWord(other[i]) size_group "word"

init python:
    def nextline():
        global poem, current_line
        current_line += 1
        poem.append([])
        renpy.restart_interaction()
    NextLine = renpy.curry(nextline)

    def previousline():
        global current_line
        current_line -= 1
        renpy.restart_interaction()
    PreviousLine = renpy.curry(previousline)

    def addword(word):
        global poem, current_line
        if (word[0] == "-"): # if we have a suffix, add on to last word
            # special case -ing onto a word ending with 'e'
            if ((poem[current_line][-1][-1] == "e") and (word == "-ing")):
                poem[current_line][-1] = poem[current_line][-1][0:-1] + word[1:]
            else:
                poem[current_line][-1] += word[1:]
        else:
            poem[current_line].append(word)
        renpy.restart_interaction()
    AddWord = renpy.curry(addword)

    def deleteword(index):
        global poem, current_line
        del poem[current_line][index]
        renpy.restart_interaction()
    DeleteWord = renpy.curry(deleteword)

    def reset(fullReset=False):
        global poem, current_line
        if (fullReset):
            poem = [[]]
            current_line = 0
        else:
            poem[current_line] = []
        renpy.restart_interaction()
    Reset = renpy.curry(reset)

    def textinput():
        new_word = renpy.input("Word?")
        addword(new_word)
    # curried up above so we can call it in a new context

style pp_label is label:
    xalign 0.5

style pp_vpgrid is vpgrid:
    spacing 5

style pp_button_text is button_text:
    size 18
    xalign 0.5

style pp_text is text:
    color "#000000"
