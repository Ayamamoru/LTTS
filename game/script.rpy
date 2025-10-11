# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Eileen")
define mc = Character("[povname]", color="#be6ae6")
define v = Character("???", color="#c8ffc8")


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
        m "regardless..."

    $ povname = "..."

    v "Your name does not matter."
    v "This is not your story."
    mc "??????????"
    #ok i think it works now
    return
