
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

default interest = "other"

transform dimmed:
    matrixcolor BrightnessMatrix(-0.1)

transform left_dimmed:
    xpos 0.0
    ypos 1.0
    matrixcolor BrightnessMatrix(-0.1)

transform right_dimmed:
    xpos 1.0
    ypos 1.0
    matrixcolor BrightnessMatrix(-0.1)

#lock in, diva
label start:
    scene bg lab general
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

    show hain pleased at dimmed
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

hide hain
show hain idea
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

show hain idea
h "Since you're here early too, you're welcome to come watch!"

show hain idea at dimmed
menu:
    "Let's do it!":
        pass
    "Sounds good.":
        pass

hide hain
show hain proud
h "Awesome!"

show hain explain
h "Glad you can join me."

show hain idea
h "It’s totally normal for things to look or feel unfamiliar, so if there’s anything confusing, feel free to ask questions!"

show hain pleased
h "If you’re curious about my perspective on what it’s like being a university student, being an undergraduate researcher, or even what it’s like being me, don’t be afraid to ask!"

#who is hain? segment
label prologue_question_scene:
    default ask_uni = False
    default ask_ugr = False
    default ask_hain = False

    show hain pleased at dimmed

    menu:
        "What's it like being a university student?" if not ask_uni:
            $ ask_uni = True
            hide hain
            jump uni_scene
        "What's it like being an undergraduate researcher?" if not ask_ugr:
            $ ask_ugr = True
            hide hain
            jump ugr_scene
        "What's it like being Hain?" if not ask_hain:
            $ ask_hain = True
            hide hain
            jump hain_intro_scene
        "Take me to the science!" if ask_uni or ask_ugr or ask_hain:
            hide hain
            jump science_start_scene

label uni_scene:
    # scene bg scope

    show hain proud
    h "Oh, I love that question!"

    show hain think
    h "I just finished my first year at university, and it's been a blast!"
    h "So, I guess..."

    show hain introduce
    h "I'm a second year now!"

    show hain idea
    h "Do you want to try and guess my major?"

    hide hain
    p "Oh! Hm..."

    label major_guess:
        default guessed_bme = False
        default guessed_hyphy = False
        default guessed_neuro = False

        menu:
            "Biomedical engineering":
                $ guessed_bme = True
                hide hain
                show hain introduce
                h "Not quite! But it was brave of you to take a chance at it."
                show hain introduce at dimmed
                jump major_guess

            "Human physiology":
                $ guessed_hyphy = True
                hide hain
                show hain introduce
                h "Not quite! But it was brave of you to take a chance at it."
                show hain introduce at dimmed
                jump major_guess

            "Neuroscience":
                $ guessed_neuro = True
                hide hain
                show hain introduce
                h "Not quite! But it was brave of you to take a chance at it."
                show hain introduce at dimmed
                jump major_guess

            "Biochemistry":
                hide hain
                show hain celebrate
                jump correct_major

        label correct_major:
            h "You got it!"

    show hain idea
    h "I'm a biochemistry major with a minor in bioengineering."

    show hain ponder
    h "It sounds like a lot of jargon, but it basically means that I get to take lots of biology, chemistry, and bioengineering classes alongside my electives!"

    show hain proud
    h "Last year, I got to take an elective where we spent a whole term analyzing the meaning behind different colors."

    show hain idea
    h "I even got to take a class where we learned how to incorporate art into STEM curriculum for K-8 students!"

    hide hain
    "(Fun fact, this is what inspired real-life Hain to make this game!)"

    show hain pleased
    h "You don't have to be a biochemistry major to work in the Worm Lab, though."

    show hain explain
    h "Regardless of what you major in, as long as you're inspired to seek answers to scientific questions, you're more than qualified!"
    h "What about you? What kinds of fields of study interest you the most?"

    show hain explain at dimmed
    menu:
        "STEM (Science, Technology, Engineering, and Math)":
            $ interest = "STEM"
        "Art":
            $ interest = "art"
        "Humanities":
            $ interest = "humanities"
        "Business":
            $ interest = "business"
        "Other":
            $ interest = "something other than STEM"
        "I'm not quite sure yet...":
            $ interest = "something other than STEM"
    hide hain
    show hain pleased
    h "Nice!"

    if interest in ["art", "humanities", "business", "something other than STEM"]:
        h "It's awesome that you're exploring science alongside your interests!"
    else:
        h "You're in the perfect place."
    
    hide hain
    "Hain walks over to a table and takes the scope cover off of the microscope."
    "She flips the switch on, and puts on gloves as she moves to a smaller room in the back of the lab with a row of incubators."
    "Opening the one marked '25 degrees Celsius', she pulls out two petri plates."

    if ask_uni == True and ask_ugr == True and ask_hain == True:
        jump science_start_scene
    if ask_uni == True or ask_ugr == True or ask_hain == True:
        show hain introduce
        "Is there anything else that you're curious about?"
        jump prologue_question_scene

label ugr_scene:
    scene bg lab general

    show hain cry
    h "What can I say? It feels like a dream."

    show hain pleased
    h "I've always wanted to do research."

    show hain explain
    h "It was actually my one big goal for freshman year of university: get into a lab."
    h "It sounds daunting, but I was lucky enough to nab an interview to start working as an undergraduate lab technician during my first term."

    show hain cry
    h "If I was given the chance to start over, I wouldn't change a thing."

    show hain cry at dimmed
    p "What does an undergraduate lab technician do?"
    p "Is it different from being an undergraduate researcher?"

    hide hain
    show hain proud
    h "Great question!"

    show hain explain
    h "Most labs only have undergraduate researcher positions."

    show hain ponder
    h "But, our lab is bigger, so I get paid to help make all the petri plates and reagents that get shared by everyone in lab."
    
    show hain explain
    h "I do research for credit."
    h "Typically, research for undergraduates is on a volunteer basis, funded through fellowships, or sometimes even paid."

    show hain think
    h "My path to research was surprisingly linear."

    show hain introduce
    h "While I'd be making plates, I'd ask folks in lab what they were working on at the moment."
    h "I'd go to our weekly lab meetings and hear presentations from our lab members."
    
    show hain proud
    h "Oh, the joy that I'd feel whenever I was able to recognize a word from their presentation that I'd heard from our conversations!"

    show hain ponder
    h "I think that my curiosity for the science that's going on in our lab was the biggest indicator that I was interested in research."

    show hain proud
    h "After almost a year of working as a technician and connecting with people in lab, I'd built up a reputation as a curious, hard-working, undergraduate with a passion for the lab's science."

    show hain explain
    h "My dream for freshman year of university was to start running my own experiments."
    h "By now, I'd worked up the courage to ask the lab's PI, or primary investigator (the head of the lab) about whether it would be possible for me to learn some lab skills that would put me in the driver's seat."

    show hain surprised
    h "You should have seen the shock on my face when he said that he and our lab manager had been talking about connecting me with a lab mentor to start doing research."

    show hain celebrate
    h "It's been absolutely awesome!"

    show hain introduce
    h "Over the summer, I've been learning some foundational skills to be able to run experiments in the lab."
    h "I've just started working on my personal project, but when I was learning new skills from scratch, I was mostly helping my lab mentor with her projecs."
    h "Now I've got my own project!"

    show hain idea
    h "But you'll get to hear more about that soon!"

    jump prologue_question_scene

label hain_intro_scene:
    show hain cry
    h "You'd think this one's the easiest to answer, but I usually never know where to start."

    show hain think at dimmed
    "Hain fiddles with the buttons on her lab coat, deep in thought."

    hide hain
    show hain ponder
    h "Ah. How about this?"

    show hain introduce
    h "I'm a scientist-artist."
    h "I'm also a storyteller at heart."

    show hain celebrate
    h "I love being able to share the enthusiasm that I have for science, the enthusiasm that I have for learning, with those around me."

    show hain explain
    h "Art is the medium through which I choose to do that."

    show hain think
    h "You know, my answer to this question was actually supposed to be me integrating some of my interests outside of science. But I can't really imagine much of my life witout science and art."
    
    show hain proud
    h "I'm grateful that they're both my hobbies and my passions."

    show hain pleased
    h "Oh, I know!"
    h "I absolutely adore my orange cat, Lulu!"
    h "He's an absolute angel. Here's a picture."

    #insert picture of lulu

    h "I also play the flute, I love to read, and I love mint chocolate ice cream. Shocker, huh?"

    #SKIP TO THE SCIENCE

    label science_start_scene: 
        hide hain

        "Hain shuffles the petri plate on the microscope stage, trying to get something into focus."
        "She's crouching as she peers into the lenses, absentmindedly nudging a chair in front of the microscope with her feet as she gets the thing info focus."
        "After a bit of messing with the ocular lenses, she stands up straight with a smile."

        show hain explain
        h "Why don't you take a look?"

        #insert worm photo!

        h "These are {i}C. elegans{/i}. Most people know them as nematodes!"
        h "They're little transparent roundworms that look a little something like this."

        h "The head is right around here."
        h "Their vulva is right around here. When they lay eggs, they come out of here!"
        h "Their tail is around here."
        h "They nautrally life on rotting fruit and in dirt. Anywhere that there's bacteria for them to eat..."

        h "The adults grow to be around 1 millimeter long, and they only life for around 2-3 weeks."
        h "They've got 100,000,000 nucleotides of DNA in their entire genome, and guess what?"

        h "{i}C. elegans{/i} are the first multicellular organism to have its entire genome sequenced in 1998 by John Sulston and his friends over at the Wellcome Sanger Institute."

        h "Even now, there are efforts to sequence the entire genomes of 959 different {i}Caenorhabditis{/i} species (an homage to the fact that there are 959 cells in an adult female {i}C. elegans{/i})."
        h "{i}Caenorhabditis{/i} is what the {i}C.{/i} stands for in {i}C. elegans!{/i} {i}Caenorhabditis{/i} are basically the bigger category, or genus, that different species, like {i}elegans{/i} are a part of."
        h "As of 2026, over 300 of these genomes have been sequenced!"

        w "Are you talking about me?"

        "[player_name] had just learned about how these worms are only about a millimeter long!"
        "[p_subject!c]'d only briefly caught the cloud of mist in the corner of their eye."
        "With comical caution, [p_subject] turned around to see the {i}C. elegans{/i} [p_subject]'d heard so much about."
        "Only..."
        "This worm was roughly the size of a toddler."

        #scene worm surprise

        h "Who...I've never..."

        menu:
            "So, this isn't normal?":
                pass
            "That's awesome!":
                pass
            "I knew that space aliens were real.":
                pass
        
        w "Hi, I'm Wormy!"

        w "I'm a close relative of {i}C. elegans, C. remanei!{/i}"
        w "I'll be handling the worm facts for our experiment today."

        menu:
            "I still don't understand...":
                pass
            "Sounds good!":
                pass
            "Are you from Mars?":
                pass
            
        w "{i}C. elegans{/i} are mostly hermaphrodites (worms with both male and female reproductive organs)."
        w "The hermaphrodites can reproduce on their own. This is called selfing. Males are usually more rare."
        w "{i}C. remanei{/i} want both male worms and female worms to reproduce."
        w "Any idea why that might be?"

        # LAB NOTEBOOK

        menu:
            "We want genetic diversity?":
                pass
            "We want offspring with genetic material from two parents?":
                pass
        
        w "Right!"
        w "For our experiment, we want baby worms from two different parents, rather than baby worms from the same worm."
        w "Like you said, if we want a worm with traits from two different worms, not having to worry about the worms selfing would make the process simpler."
        w "So, for the purposes of our experiment, we'll be using {i}C. remanei{/i}."

        menu:
            "That makes sense.":
                "[player_name] turns to Hain."
                p "This is all cool science, but why do we do it in the first place?"
                pass
            "That's so interesting!":
                "[player_name] turns to Hain."
                p "I'm curious. What inspires people to do this kind of science?"
                pass

        h "That's a great question!"
        h "Of course everyone has their own answers, and you're already heard a little bit of mine."
        h "Hopefully this little experiment will help you explore that your 'why science' could be too!"

        h "Well, that was quite a bit of exposition, wasn't it?"
        h "Here, come sit in this chair and adjust the microscope focus to your liking. Let's do some science!"

        


        

        


    
            
            






return