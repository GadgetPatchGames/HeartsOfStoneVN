## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## Resources ###################################################################

## Transitions #################################################################

# Custom "with" Transitions

define quickdissolve = Dissolve(0.25)
define starout = ImageDissolve("wipes/star.png", 0.5)
define starin = ImageDissolve("wipes/star.png", 0.5, reverse=True)

# Custom "at" Positions

transform close(x=0, y=0, time=0):
    ease time xcenter 0.5+(x*0.08333) ycenter 0.83333+(-y*0.08333) zoom 2

transform mid_close(x=0, y=0, time=0):
    ease time xcenter 0.5+(x*0.08333) ycenter 0.70833+(-y*0.08333) zoom 1.5

transform mid(x=0, y=0, time=0):
    ease time xcenter 0.5+(x*0.08333) ycenter 0.58333+(-y*0.08333) zoom 1

transform mid_far(x=0, y=0, time=0):
    ease time xcenter 0.5+(x*0.08333) ycenter 0.5+(-y*0.08333) zoom 0.66667

transform far(x=0, y=0, time=0):
    ease time xcenter 0.5+(x*0.08333) ycenter 0.45833+(-y*0.08333) zoom 0.5

# Animation

define from_right = MoveTransition(1)

transform punch:
    ease 0.025 xanchor 0.51
    ease 0.025 xanchor 0.49
    ease 0.03333 xanchor 0.51
    ease 0.03333 xanchor 0.49
    ease 0.05 xanchor 0.51
    ease 0.05 xanchor 0.49
    ease 0.06667 xanchor 0.51
    ease 0.06667 xanchor 0.49
    ease 0.08333 xanchor 0.51
    ease 0.08333 xanchor 0.49
    ease 0.1 xanchor 0.51
    ease 0.1 xanchor 0.5

transform animate_shake:
    ease 0.075 xanchor 0.51
    ease 0.075 xanchor 0.49
    repeat

transform animate_shake_left:
    linear 0.125 xanchor 0.635
    linear 0.125 xanchor 0.615
    repeat

transform animate_shake_right:
    linear 0.125 xanchor 0.385
    linear 0.125 xanchor 0.365
    repeat

# 0.91667
# 0.875
# 0.83333
# 0.79167
# 0.75
# 0.70833
# 0.66667
# 0.625
# 0.58333
# 0.54167
# 0.5
# 0.45833
# 0.41667
# 0.375
# 0.33333

# 1
# 0.9167
# 0.8333
# 0.75
# 0.6667
# 0.5833
# 0.5
# 0.4167
# 0.3333
# 0.25
# 0.1167
# 0.0833
# 0

# 12 values (+/- 0.0833)
# 0.0416
# 0.125
# 0.2083
# 0.2916
# 0.375
# 0.4583
# 0.5416
# 0.625
# 0.7083
# 0.7916
# 0.875
# 0.9583

# 6 values midpoint (+/- 0.1667)
# 0.0833
# 0.25
# 0.4167
# 0.5833
# 0.75
# 0.9167

## Images ######################################################################

# Flat Colors
image black = "#000000"
image grey = "#808080"
image white = "#FFFFFF"
image red = "#FF0000"
image green = "#00FF00"
image blue = "#0000FF"
image cyan = "#00FFFF"
image yellow = "#FF00FF"
image magenta = "#FFFF00"

# Background Images
image lecture back= "bg/lecture_back.png"
image lecture front = "bg/lecture_front.png"
image space = "bg/space.png"
image space terra = "bg/space_terra.png"
image terra = "bg/surface_terra.png"
image desert = "bg/surface_desert.png"
image plant = "bg/surface_plant.png"

## Sprites #####################################################################

# Miscellaneous
image shuttle = "sprite/shuttle.png"

# Slate
image slate = "sprite/slate.png"

# Amber
image amber = "sprite/amber.png"
image amber joke = "sprite/amber_joke.png"

# Quartzite
image quartzite = "sprite/quartzite.png"
image quartzite joke = "sprite/quartzite_joke.png"

# Halite
image halite = "sprite/halite.png"
image halite joke = "sprite/halite_joke.png"


## Characters ##################################################################

define narrator = Character(None,
    who_color="#808080", who_outlines=[ (2, "#000000") ],
    what_color="#808080", what_outlines=[ (2, "#000000") ],
    window_background=Frame("GUI/frame_base.png", 80, 80),
    namebox_background=Frame("GUI/namebox_base.png", 80, 80)
)

define s = Character("Slate",
    who_color="#9966AA", who_outlines=[ (2, "#000000") ],
    what_color="#FFFFFF", what_outlines=[ (2, "#000000") ],
    window_background=Frame("GUI/frame_slate.png", 80, 80),
    namebox_background=Frame("GUI/namebox_slate.png", 80, 80)
)

define q = Character("Quartzite",
    who_color="#FFFFFF", who_outlines=[ (2, "#000000") ],
    what_color="#FFFFFF", what_outlines=[ (2, "#000000") ],
    window_background=Frame("GUI/frame_quartzite.png", 80, 80),
    namebox_background=Frame("GUI/namebox_quartzite.png", 80, 80)
)

define h = Character("Halite",
    who_color="#3399AA", who_outlines=[ (2, "#000000") ],
    what_color="#FFFFFF", what_outlines=[ (2, "#000000") ],
    window_background=Frame("GUI/frame_halite.png", 80, 80),
    namebox_background=Frame("GUI/namebox_halite.png", 80, 80)
)

define a = Character("Amber",
    who_color="#FF9933", who_outlines=[ (2, "#000000") ],
    what_color="#FFFFFF", what_outlines=[ (2, "#000000") ],
    window_background=Frame("GUI/frame_amber.png", 80, 80),
    namebox_background=Frame("GUI/namebox_amber.png", 80, 80)
)

## Transforms move sprites


## Transforms move sprites

## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Hearts of Stone")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "0.1"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""Hearts of Stone is a Visual Novel, created for Rainbow Jam 2018.

    Credits:

    - Characters: Sheets

    - Music: CSJ

    - Scripting: Spoid
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "HeartsOfStone"


## These control the width and height of the screen.


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "hide"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "HeartsofStone-1537837884"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
