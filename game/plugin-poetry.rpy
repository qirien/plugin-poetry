screen plugin_poetry:
    frame:
        style_prefix "pp"
        xpadding 50
        ypadding 50
        xfill True
        yalign 0.0
        background "images/stars.jpg"
        vbox:
            vbox:
                hbox:
                    label "Poem"
                    null width 200
                    textbutton "Next Line" action NextLine()
                    textbutton "Done" action Return()
                vbox:
                    for i in range(0, len(poem)):
                        hbox:
                            for j in range(0, len(poem[i])):
                                text poem[i][j]
                                text " "
            hbox:
                spacing 10
                xfill True
                ypos 50
                vbox:
                    label "Nouns"
                    vpgrid:
                        cols 3
                        for i in range(0, len(nouns)):
                            textbutton nouns[i] action AddWord(nouns[i]) size_group "word"

                vbox:
                    label "Adjectives"
                    vpgrid:
                        cols 3
                        for i in range(0, len(adjectives)):
                            textbutton adjectives[i] action AddWord(adjectives[i]) size_group "word"

                vbox:
                    label "Verbs"
                    vpgrid:
                        cols 2
                        for i in range(0, len(verbs)):
                            textbutton verbs[i] action AddWord(verbs[i]) size_group "word"

                vbox:
                    label "Other"
                    vpgrid:
                        cols 2
                        for i in range(0, len(other)):
                            textbutton other[i] action AddWord(other[i]) size_group "word"

init python:
    def nextline():
        global poem, current_line
        current_line += 1
        poem.append([])
    NextLine = renpy.curry(nextline)

    def addword(word):
        global poem, current_line
        poem[current_line].append(word)
        renpy.restart_interaction()
    AddWord = renpy.curry(addword)


style pp_label is label:
    xalign 0.5
