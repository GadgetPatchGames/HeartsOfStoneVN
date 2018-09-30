# The main script of the game goes in this file.

## Function Variables ##########################################################

define hide1 = False
define hide2 = False
define hide3 = False
define hide4 = False
define hide5 = False

python early:

    def reset_hide(value=False):
        hide1 = value
        hide2 = value
        hide3 = value
        hide4 = value
        hide5 = value
        return

init python:

    def right_tag(tag, argument, contents):

        size = int(argument) * 20

        return [
                (renpy.TEXT_TAG, u"size={}".format(size)),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"),
            ]

    config.custom_text_tags["right"] = right_tag

## Start #######################################################################

default Gender = "Non-binary"
default gender = "non-binary"
default Person = "Person"
default person = "person"
default People = "People"
default people = "people"
default Friend = "Friend"
default friend = "friend"
default Pal = "Pal"
default pal = "pal"
default Dude = "Dude"
default dude = "dude"
default Them = "Them"
default them = "them"
default They = "They"
default they = "they"
default Their = "Their"
default their = "their"
default Theirs = "Theirs"
default theirs = "theirs"
default Theirself = "Theirself"
default theirself = "theirself"
default Kid = "Kid"
default kid = "kid"
default Are = "Are"
default are = "are"
default Were = "Were"
default were = "were"
default Have = "Have"
default have = "have"
default re = "'re"
default ve = "'ve"
default Mx = "Mx."
default Mix = "Mix"
default mix = "mix"

label start:

    # Intro; out of character info, set gender, etc.

    scene space

    "Thanks for playing Hearts of Stone!\nThis Visual Novel was made in Ren'Py, for Rainbow Jam 2018.\nProject Source on {a=github.com/GadgetPatchGames/HeartsOfStoneVN}GitHub{/a}"

    "Art: Adrian 'Sheets' PaperHelmet (relevant link)\nMusic: CSJ Lastname (relevant link)\nScripting: Day 'Starscorpion' Holdampf (relevant link)"

    menu:
        "Quick question: is your character a guy or a gal?"

        "Guy":
            $ Gender = "Male"
            $ gender = "male"
            $ Person = "Man"
            $ person = "man"
            $ People = "Men"
            $ people = "men"
            $ Friend = "Sir"
            $ friend = "sir"
            $ Pal = "Buddy"
            $ pal = "buddy"
            $ Dude = "Guy"
            $ dude = "guy"
            $ Them = "Him"
            $ them = "him"
            $ They = "He"
            $ they = "he"
            $ Their = "His"
            $ their = "his"
            $ Theirs = "His"
            $ theirs = "his"
            $ Theirself = "Himself"
            $ theirself = "himself"
            $ Kid = "Boy"
            $ kid = "boy"
            $ Are = "Is"
            $ are = "is"
            $ Were = "Was"
            $ were = "was"
            $ Have = "Has"
            $ have = "has"
            $ re = "'s"
            $ ve = "'s"
            $ Mx = "Mr."
            $ Mix = "Mister"
            $ mix = "mister"

        "Gal":
            $ Gender = "Female"
            $ gender = "female"
            $ Person = "Woman"
            $ person = "woman"
            $ People = "Women"
            $ people = "women"
            $ Friend = "Ma'am"
            $ friend = "ma'am"
            $ Pal = "Lady"
            $ pal = "lady"
            $ Dude = "Gal"
            $ dude = "gal"
            $ Them = "Her"
            $ them = "her"
            $ They = "She"
            $ they = "she"
            $ Their = "Her"
            $ their = "her"
            $ Theirs = "Hers"
            $ theirs = "hers"
            $ Theirself = "Herself"
            $ theirself = "herself"
            $ Kid = "Girl"
            $ kid = "girl"
            $ Are = "Is"
            $ are = "is"
            $ Were = "Was"
            $ were = "was"
            $ Have = "Has"
            $ have = "has"
            $ re = "'s"
            $ ve = "'s"
            $ Mx = "Ms."
            $ Mix = "Miss"
            $ mix = "miss"

        "Nope":
            pass

    show slate at close
    "Pronoun Testbed: [Their] gender is [Gender]. You might call [them] \"[Mx] Slate\", [friend], [pal], or just \"some [dude]\". [They][ve] been in space since [they] [were] a [kid], and [are] a young rock-[person]."
    "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

    hide slate
    
    # This begins the Intro scene.
    jump intro

    # This ends the game.
    return