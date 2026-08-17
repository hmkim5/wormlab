# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define h = Character('Hain')


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hain introduce

    # These display lines of dialogue.
    
    h "Welcome to the Worm Lab!"

    h "My name is Hain, and this is a test-run."

    show hain idea

    h "Now we're going to try and see if we can play a video."

    show hain ponder
    
    h "Is that okay with you?"

    menu:
        'Yes':
            $ renpy.movie_cutscene('videos/uhreal.webm')
        'No':
            show hain cry

            h "But I worked so hard on it!"

            show hain pleased

            h "No biggie."

    h "Done!"

    # This ends the game.

    

    return

