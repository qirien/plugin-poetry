screen poetry_display:
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        background "images/stars.jpg"
        frame:
            yfill True
            background "#aaaaaa"
            hbox:
                xfill True
                vbox:
                    spacing 20
                    hbox:
                        label "Poems" text_size 50
                    vbox:
                        spacing 30
                        for count in range(0, len(poems)):
                            vbox:
                                spacing 5
                                for i in range(0, MAX_LINES):
                                    hbox:
                                        spacing 5
                                        if (i < len(poems[count])):
                                            for j in range(0, len(poems[count][i])):
                                                textbutton poems[count][i][j] action Confirm("Delete this poem?", DeletePoem(count))

                vbox:
                    xalign 0.8
                    spacing 5
                    textbutton "Add New Poem" action Jump("make_poem") sensitive (len(poems) < MAX_POEMS)
                    textbutton "Screenshot" action Screenshot()
                    textbutton "Save" action ShowMenu("save")
                    textbutton "Quit" action Return()

init python:
    def delete_poem(poem_number):
        global poems
        poems.remove(poems[poem_number])

    DeletePoem = renpy.curry(delete_poem)

style pd_button_text is button_text:
    size 16
