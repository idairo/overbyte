screen CineHalf1():
    zorder -1
    layer "master"
    add "cinebar/cinebar.png" at t_CineHalf_top

screen CineHalf2():
    zorder 1
    layer "master"
    add "cinebar/cinebar.png" at t_CineHalf_bot

transform t_CineHalf_top():
    xpos 0
    ypos -1080
    easein_circ v_TransitionTime ypos -900
    on hide:
        easein_circ v_TransitionTime ypos -1080

transform t_CineHalf_bot():
    xpos 0
    ypos 1080
    easein_circ v_TransitionTime ypos 700
    on hide:
        easein_circ v_TransitionTime ypos 1080





screen CineFull():
    zorder 101
    # layer "master"
    add "cinebar/cinebar.png" at t_CineFull_top
    add "cinebar/cinebar.png" at t_CineFull_bot

transform t_CineFull_top():
    xpos 0
    ypos -1080
    easein_circ v_TransitionTime ypos -500 # -540
    on hide:
        easein_circ v_TransitionTime ypos -1080

transform t_CineFull_bot():
    xpos 0
    ypos 1080
    easein_circ v_TransitionTime ypos 500 # 540
    on hide:
        easein_circ v_TransitionTime ypos 1080





label ShowCineHalf:
    show screen CineHalf1
    show screen CineHalf2
    pause v_TransitionTime
    return
label HideCineHalf:
    window hide
    hide screen CineHalf1
    hide screen CineHalf2
    pause v_TransitionTime
    return
label ShowCineFull:
    show screen CineFull
    pause v_TransitionTime
    return
label HideCineFull:
    hide screen CineFull
    pause v_TransitionTime
    return