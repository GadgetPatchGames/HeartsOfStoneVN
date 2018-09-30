# The way I was roughing out the intro is like...
# - Quartz and Slate, meeting in cafe, before senior year orientation/homeroom.
# - Establish their friendship, Quartz asks about plans for post graduation, Slate has none.
# - Hint at concern for Slate not graduating, and them not being on the same team/crew/whatever.
# - Quartz expresses concern for Slate not connecting with any friends in class, but doesn't bully 'em.
# - Has to head off, wants to check in with other students (establish sort of Class Rep persona)
# - Slate has some thoughts to themselves about this, sets the intention to figure out their goal in class, and to get to know their classmates.
# Then we have a scene in Homeroom, introducing Pyrite, basic structure of game loop (Classes, Weekends, and Away Missions cycle)
# Then some scenes to introduce the rest of the main cast, in groups, etc.
# I always write awakenings and amnesia, and I want to avoid that. just do In Media Res
# Establish things as relatable
# 
# To that end, I was going to suggest that their d1 is tied to New Kid Pallasite
# unexpectedly, Slate is introduced to them and asked to show them around by Quartz
# Quartz motive to get you to know new people, and get you more involved, and it's a low-cost thing since they're new too.
# Pallasite's perspective is a proxy for the audience as they get a feel for the world these mineralised butts live in
# Quartz/Teach would have plenty of motives to lump them together
# 
# I like the idea of doing a rough intro for a few other characters, then after class they are told to show Meteorite/Pallasite around.
# So it's a little special. So they stand out more
# Maybe they didn't show up in time for orientation, which is why teach didn't introduce them
# And it sets up Pallasite as a great foil for the PC, since the player has this mission to get to know everyone, and Pallasite is intentionally distant because INTRIGUE
# 
# We hit the main friend relationship to ground the player, the main game loop in class, and establish the foil and the setting.
# And it's all true to character
# good stuff

## Intro #######################################################################

label intro:

    scene space terra with starout

    show shuttle at mid (-8.5, -2)

    show shuttle at far (0, 2, time=6)

    pause 5

    label terra_start:

        scene terra with starout

        pause 0.5

        "You and your classmates step out of the shuttle."
        "The soil crunches sharply under your shoes as you disembark. Each footfall breaks through a fine crust, built up over many long, silent years."
        
        show quartzite at mid (8)
        show quartzite at mid (0, time=2.5)
        q "Hard to believe people used to live down here, huh Slate?" (name=None)
        
        "You recognize the voice of your friend, Quartzite. They wave to you, as they walk over"
        q "So, this is Terra. \"The Cradle of Life.\" Apparently this all used to be covered in green plants, blue oceans of water..."
        s "And all that's left now is a bunch of red dirt."
        q "Yeah. Though {i}technically{/i} there's still some microscopic life under that red dirt? But nothing else can survive."
        
        menu terra1:
            extend ""
            "What happened here, anyway?" if hide1 == False:
                s "What happened here, anyway?"
                q "You don't know? But we just covered this in Planetology..."
                s "I guess I wasn't paying attention that day?"
                q "Come on, [kid]. This stuff is important!"
                s "Sure it is. That's why I'm asking about it now!"
                "Quartz rolls their eyes. You've known one another long enough that they're used to this sort of thing by now."
                q "In that case, our best guess is that the planet got too hot, for some reason or other."
                q "Once that happened, it kicked off a bunch of planet-wide changes that kept things getting hotter and hotter."
                q "Eventually, most of the water either boiled off, or drained away below the crust. Now, nothing much can live here anymore."
                $hide1 = True;
                jump terra1

            "But we're here, and we're alive. (->)":
                s "But we're here, and we're alive."
                q "That's true. Guess it takes more than a little heat to keep us down, huh?"

            "Kinda sad, isn't it? (->)":
                s "Kinda sad, isn't it?"
                q "Yeah... waste of a perfectly good planet."
                "You both take a melancholy look at the surrounding wastelands."
        
        "Other students mill around in small groups, chatting amongst themselves. You hear someone laugh in the distance."
        s "Why did we come down here, anyway?"
        q "I don't really know."
        s "Aren't you the Class Representative? Shouldn't you know these things?"
        q "All Professor Pyrite told me was that it was a mandatory activity. "
        "It was a last minute change of plan."
        "You remember hearing something about that."

        # Space station is wearing down. Pyrite organized last minute Planetside training.
        # Gold made decision to begin looking for a new homeworld, and need students to survey habitable worlds.
        # Training splits students into groups, to recover survey probes safely. Pick a group. One group does nothing.
        # Through course of converation, get to know members of each group.
        # They can boost two of your skills by 1 (whatever that character is best known for.) Preempt the challenge.
        
        q "She never said! You know how spacy the Professor is."
        

return