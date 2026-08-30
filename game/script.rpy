
# variables for characters
define h = Character('Hain')
define p = Character("[player_name]")
define w = Character('Wormy')

# variables for pronouns
default p_subject = "they"    # subject : he, she, they
default p_object = "them"    # object : him, her, them
default p_possessive = "their" # possessive : his, hers, their
default p_possessive_obj = "theirs" # possessive object : theirs..
default p_verb = "are"        # is/are
default p_verb_contract = "'re" # this can't be the simplest way to do this

#lock in, diva
label start:
    scene bg room

    "The soft hum of equipment feels like white noise."
    "Early in the morning, rays of sun shine through the window screen and the whole place feels a little magical."
    "With a flip of the light switch, the lab comes to life."

    show hain celebrate

    h "Good morning, worms!"

    hide hain

    "Hain is the first person in lab today."
    "It’s quiet and there’s a comforting calm in the ambience of it all."
    "Then, the door opens and..."

    show hain pleased

    h "Oh, hi there! You must be the lab's new undergraduate researcher!"
    h "What's your name again?"

    hide hain
    
    python:
        player_name = renpy.input("Player name (20 character limit):", length=20)
        player_name = player_name.strip()
    
        if not player_name:
            player_name = "Player"

menu choose_pronouns:

    "He / Him":
        $ p_subject = "he"
        $ p_object = "him"
        $ p_possessive = "his"
        $ p_verb = "is"
        $ p_verb_contract = "'s"

    "She / Her":
        $ p_subject = "she"
        $ p_object = "her"
        $ p_possessive = "her"
        $ p_verb = "is"
        $ p_verb_contract = "'s"

    "They / Them":
        $ p_subject = "they"
        $ p_object = "them"
        $ p_possessive = "their"
        $ p_verb = "are"
        $ p_verb_contract = "'re"

h "Nice to meet you, [player_name]!"

show hain introduce

h "My name's Hain! My pronouns are she/her, and I'm an undergraduate researcher in the Worm Lab!"

show hain ponder

h "It's pretty early in the morning so there's not a lot of people here yet."
h "Usually it's pretty lively here! There's around twenty people in our lab."

show hain pleased

h "It feels like we're all one big family."

show hain explain

h "I was actually just about to run an experiment."
h "Since you're here early too, you're welcome to come watch!"

menu:
    "Let's do it!":
        pass
    "Sounds good.":
        pass

show hain proud

h "Awesome!"

show hain explain

h "Glad you can join me."

show hain idea

h "It’s totally normal for things to look or feel unfamiliar, so if there’s anything confusing, feel free to ask questions!"

show hain pleased

h "If you’re curious about my perspective on what it’s like being a university student, being an undergraduate researcher, or even what it’s like being me, don’t be afraid to ask!"

#who is hain? segment
menu:
    "What's it like being a university student?":
        jump uni_scene
    "What's it like being an undergraduate researcher?":
        jump ugr_scene
    "What's it like being Hain?":
        jump hain_intro_scene

label uni_scene:
    # scene bg scope

    show hain proud

    h "Oh, I love that question!"

    show hain think

    h "I just finished my first year at university, and it's been a blast!"
    h "So, I guess..."

    show hain introduce

    h "I'm a second year now!"

    h "Do you want to try and guess my major?"

    p "Oh! Hm..."

    label major_guess:
        default guessed_bme = False
        default guessed_hyphy = False
        default guessed_neuro = False

        menu:
            "Biomedical engineering":
                $ guessed_bme = True
                h "Not quite! But it was brave of you to take a chance at it."
                jump major_guess

            "Human physiology":
                $ guessed_hyphy = True
                h "Not quite! But it was brave of you to take a chance at it."
                jump major_guess

            "Neuroscience":
                $ guessed_neuro = True
                h "Not quite! But it was brave of you to take a chance at it."
                jump major_guess

            "Biochemistry":
                jump correct_major

        label correct_major:
            h "You got it!"

    h "I'm a biochemistry major with a minor in bioengineering."
    h "It sounds like a lot of jargon, but it basically means that I get to take lots of biology, chemistry, and bioengineering classes alongside my electives!"
    h "Last year, I got to take an elective where we spent a whole term analyzing the meaning behind different colors."
    h "I even got to take a class where we learned how to incorporate art into STEM curriculum for K-8 students!"

    "(Fun fact, this is what inspired real-life Hain to make this game!)"

    h "You don't have to be a biochemistry major to work in the Worm Lab, though."
    h "Regardless of what you major in, as long as you're inspired to seek answers to scientific questions, you're more than qualified!"

    h "What about you? What kinds of fields of study interest you the most?"






return