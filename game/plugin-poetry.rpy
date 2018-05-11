screen plugin_poetry:
    frame:
        xpadding 50
        ypadding 50
        xfill True
        yalign 0.5
        vbox:
            vbox:
                hbox:
                    label "Poem"
                    textbutton "Next Line" action NextLine()
                    textbutton "Done" action Return()
                vbox:
                    for i in range(0, len(poem)):
                        hbox:
                            for j in range(0, len(poem[i])):
                                text poem[i][j]
                                text " "

            hbox:
                vbox:
                    label "Nouns"
                    for i in range(0, len(nouns)):
                        textbutton nouns[i] action AddWord(nouns[i])

                vbox:
                    label "Adjectives"
                    for i in range(0, len(adjectives)):
                        textbutton adjectives[i] action AddWord(adjectives[i])

                vbox:
                    label "Verbs"
                    for i in range(0, len(verbs)):
                        textbutton verbs[i] action AddWord(verbs[i])

                vbox:
                    label "Other"
                    for i in range(0, len(other)):
                        textbutton other[i] action AddWord(other[i])

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
