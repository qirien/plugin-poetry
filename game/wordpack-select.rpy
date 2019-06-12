screen wordpack_select(wordpack_list):
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        background "images/stars.jpg"
        frame:
            xpadding 50
            ypadding 50
            yfill True
            xfill True
            vbox:
                spacing 20
                label "Wordpack Selection" text_size 50 xalign 0.5
                text "What wordpacks would you like to use?\nYou may choose as many as you wish, but using at least Basic Words is recommended."
                hbox:
                    spacing 100
                    vbox:
                        label "Available Words"
                        vpgrid:
                            cols 3
                            for i in range(0, len(wordpack_list)):
                                textbutton wordpack_list[i].capitalize() action AddToSet(chosen_wordpacks, wordpack_list[i]) size_group "wordpack"
                    vbox:
                        xsize 300
                        label "Chosen Words" xalign 0.5
                        vpgrid:
                            cols 3
                            for i in range(0, len(chosen_wordpacks)):
                                textbutton chosen_wordpacks[i].capitalize() action RemoveFromSet(chosen_wordpacks, chosen_wordpacks[i]) size_group "wordpack"

                    vbox:
                        label ""
                        textbutton "Done" action Return(chosen_wordpacks)