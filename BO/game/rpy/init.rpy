# ---------- Variables ----------
init -9999:
    define v_TransitionTime = 1.2
    define v_xpos_Center = 0.5
    define v_xpos_Left = 0.3
    define v_xpos_Right = 0.7

# ---------- Transitions ----------
init -2:
    transform t_GoIn():
        xanchor 0.5
        ypos 0
        xpos v_xpos_Center - 0.1
        easein_circ v_TransitionTime alpha 1.0 xpos v_xpos_Center
    transform t_MoveToCenter():
        easein_circ v_TransitionTime alpha 1.0 xpos v_xpos_Center
    transform t_GoInLeft():
        xanchor 0.5
        ypos 0
        xpos v_xpos_Left - 0.1
        easein_circ v_TransitionTime alpha 1.0 xpos v_xpos_Left
    transform t_MoveToLeft():
        easein_circ v_TransitionTime alpha 1.0 xpos v_xpos_Left
    transform t_GoInRight():
        xanchor 0.5
        ypos 0
        xpos v_xpos_Right + 0.1
        easein_circ v_TransitionTime alpha 1.0 xpos v_xpos_Right
    transform t_MoveToRight():
        easein_circ v_TransitionTime alpha 1.0 xpos v_xpos_Right
    transform t_GoOut():
        easein_circ v_TransitionTime alpha 0.0 xoffset -50

# ---------- Window Config ----------
init python:
    config.physical_width = 1280   # Default physical window size 1024 / 1280
    config.physical_height = 720   # Default physical window size 576  / 720
#     config.gl_resize = False       # Disable resizable window

# ---------- Splash Screen ----------
label splashscreen:
    # https://www.renpy.org/doc/html/splashscreen_presplash.html
    scene black
    with Pause(1)
    play sound "audio/typewriter-soft-click.mp3"
    show splash with dissolve
    with Pause(2)
    scene black with dissolve
    with Pause(1)
    return

# ---------- Miscellaneous ----------
init -1 python:
    # -----
    # Example Usage (under screen > textbutton):
    # action Function(initResetDefaultPref)
    def initResetDefaultPref():
        _preferences.skip_after_choices = False
        _preferences.skip_unseen = False
        _preferences.text_cps = 60
        _preferences.afm_time = 15
    # -----
    # Example Usage (under label):
    # $ changeTextbox("gui/textbox.png")
    def changeTextbox(textbox_image_path="gui/textbox.png"):
        style.window.background = Image(textbox_image_path, xalign=0.5, yalign=1.0)
        style.rebuild()
        renpy.restart_interaction()
    # -----
    # Example Usage (under label):
    # $ changeFont("fonts/Rubik.ttf")
    def changeFont(font_path="fonts/Rubik.ttf"):
        style.say_label.font = font_path
        style.say_dialogue.font = font_path
        style.rebuild()
        renpy.restart_interaction()
    # -----
    # Example Usage (define character):
    # Character("Name", callback=SFX_Dialogue)
    def SFX_Dialogue(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/typewriter-soft-click.mp3", channel="sound", loop=True, relative_volume=0.2)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    # -----
define config.menu_include_disabled = True