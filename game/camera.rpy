
#####################################################
# Python code to take screenshots, place them in the
# "Photos" directory with a unique timestamp-based
# filename.
# TODO: opening and sharing screenshots
#####################################################

init python:
    import os
    from datetime import datetime

    PHOTO_DIRECTORY = config.gamedir + "/Photos/"
    def take_picture():
        # Make the directory if needed
        if(os.path.isdir(PHOTO_DIRECTORY) == False):
            os.mkdir(PHOTO_DIRECTORY)

        # Setup the filename
        now = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename =  "Screenshot-" + str(now) + ".jpg"

        # Take the screenshot
        result = renpy.screenshot(PHOTO_DIRECTORY + filename)
        if (result):
            photos.append(filename)
            renpy.notify("Screenshot Saved!  " + filename)
            return filename
        else:
            renpy.notify("Could not take screenshot!  " + filename)
            return None                

    # Code to maybe open the photos in whatever the user's photo program is
    import sys, os, subprocess
    def open_file(filename):
        #webbrowser.open("r.txt")
        if sys.platform == "win32":
            os.startfile(filename)
            renpy.notify("windows opening")
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])
            renpy.notify("not windows opening")
        return

#####################################################
# END PYTHON
#####################################################


# Ren'Py helped functions to call the Python functions

label open_photo(pic):
    $ open_file(pic)
    return

label photo():
    window hide
    $ renpy.pause(0.3)
    $ pic = take_picture()

    window auto 
    return

label show_photo_album:
    window hide
    call screen photo_album
    window auto
    return

# Display all the photos taken
screen photo_album():
    frame:
        vbox:
            area (60, 50, 1150, 620)
            yfill True
            hbox:
                xfill True
                yfill True
                frame:
                    yfill True
                    use photo_album_grid

screen photo_album_grid():
    vbox:
        label "Photo Album"

        vpgrid:
            cols 3
            spacing 5
            mousewheel True
            scrollbars "vertical"
            side_xalign 0.5
            ysize 510

            for photo in photos:
                $ photo_file = "Photos/" + photo
                imagebutton:
                    idle photo_file
                    hover photo_file
                    at thumbnail#, highlight_imagebutton
                    action Show("show_photo", irisout, photo_file)

        textbutton "Return" action Return() xalign 0.5 yalign 0.5

# Show one photo, full screen. 
# When you click, hide it.
# TODO: Add deleting photos, sharing photos?
screen show_photo(photo):
    imagebutton:
        idle photo
        hover photo
        action Hide("show_photo", irisin)
        at full_screen