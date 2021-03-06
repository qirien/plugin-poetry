##
# You can change the look and feel of the poetry buttons and boards here
##

style pp_vpgrid is vpgrid:
    spacing 5

style pp_text is text:
    color "#000000"

style pp_button:
    padding (5,5,8,8)

style pp_button_text:
    size 18
    xalign 0.5
    idle_color "#000000"
    insensitive_color "#000000"
    hover_color "#464646"

style pp_label is label:
    xalign 0.5

style pp_label_text is label_text:
    color "#464646"

style pp_frame is frame:
    background "gui/fridge.png"

##
# Next follows variants for mobile devices
##

style pps_vpgrid is pp_vpgrid:
    spacing 10

style pps_text is pp_text
style pps_button is pp_button
style pps_button_text is pp_button_text:
    size 28

style pps_label is pp_label
style pps_label_text is pp_label_text
style pps_frame is pp_frame


transform randomize:
    choice:
        rotate -2
    choice:
        rotate 2
    choice:
        rotate -3
    choice:
        rotate 3
    choice:
        rotate 0

