# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Eileen")
define mc = Character("[povname]", color="#be6ae6")
define v = Character("???", color="#c8ffc8")

define persistent.played_more = 0

init python:
    if persistent.played_more is None:
        persistent.played_more = 0

# The game starts here.


label start:


    v "Testing!"

    $ povname = renpy.input("What is your name?", length=50)
    $ povname = povname.strip()

    if not povname:
        $ povname = "..."

    mc "my name is-"
    

    if povname.lower() in ["manly", "manlybadasshero", "manly badass hero", "hero", "badasshero"]:
        m "That's a funny coincidence..."
        m "Perhaps you have an... empty soul?"
        m "regardless..."

    if povname.lower() in ["Kaylee", "kaylee", "Kay", "kay"]:
        m "That's weird"
        m "Is this... the person who goes by 'IS THAT KAYLEE FROM HIT GAME REAL LIFE?!'?."
        m "Funny to see you here, Fawn"
        m "regardless..."

    if povname.lower() in ["Fox", "Harrow", "Foxy"]:
        m "Strange"
        m "What an unusual encounter, Fox"
        m "What are you doing here?"
        m "regardless..."

    if povname.lower() in ["Otter", "June", "Jun-yi", "Jujune"]:
        m "Strange"
        m "Funny to see you here, June"
        m "What are you doing here?"
        m "regardless..."

    #NOTE - I need to add more to this... for all the other characters really

    $ povname = "..."

    v "Your name does not matter."
    v "This is not your story."
    mc "??????????"
    #ok i think it works now

    if persistent.played_more >= 1:
        "Back again? No, please, not this..."
    "A sharp headache. The pulsing kind. You know the feeling."
    "A slight ringing in your ears, and a sense of nausea."
    "Your intuition tells you that your vision will be fuzzy, once you open your eyes."
    "You open your eyes, and sure enough, the world around you is blurry and out of focus."
    "Even then though, there's something off about the environment."
    "The air is thick and heavy, and the smell of damp earth fills your nostrils."
    "Unease slowly sinks in... not too strong, but it's there."
    "That familiar hot wave of anxiety washes over you... That feeling of being lost again."
    "You try to recall how you got here, but your memory is hazy and fragmented."
    "Frustrating as it is, you've gotten used to this feeling of memory loss"
    "You struggle a little getting up, with the world still spinning... Not that it helps the nausea."
    "You steady yourself against a nearby tree, taking deep breaths to calm your breathing a little."
    "A fair attempt to keep the panic away."
        if persistent.played_more >= 1:
            "Good to know some things never change."
            "A shame. It's a futile attempt."
    "Regardless, you can't exactly remember how you came to tumble into the middle of a forest"

    if persistent.played_more >= 1:
        "Good riddance, maybe"
    #REVIEW - HEY SO THIS LOWK SUCKS>>> NEEDS A HUGE REWRITE
menu_1:
    "Check your belongings":
        jump inventory_check

label inventory_check:
    "There doesn't seem to be much on you."
    "The thought to check your wrist for your watch immediately crosses your mind."
    "Thankfully, the familiar pressure of the watch on your wrist confirms that it's still there."
    "There doesn't seem to be much else on you, but you find a small field notebook in your pocket, along with what you think was your favorite pen"
    "Unfortunately, the notebook is nearly filled with scribbles and doodles, but there are at least 3 blank pages left."
    "It may be usable later"

    "Having nothing more to check, you place the notebook back in your pocket."
    "You look around."
    "You remember watching a video about survival on YouTube once, when you were rabbitholing through random videos."
    "The main tip was to find a highway"
    "There doesn't seem to be any highways around."
    "There is a faint sound of running water nearby though."

menu_2:
    "Head towards the sound of water":
        jump trail
    "Look for a road":
        jump highway

label trail:
    "There doesn't seem to be much around."
    "Trees crowd your vision and the forest doesn't seem to be showing any signs of ending"
    "You walk gingerly towards the sound of water."
    "The sound grows louder as you walk closer"
    "Eventually, it seems to be right ahead of you"
    "..."
    "..."
    "There is no stream"
    "The sound vanishes..."
    "But, there is a faint trail where the stream should've been."



    $ persistent.played_more += 1
    return
