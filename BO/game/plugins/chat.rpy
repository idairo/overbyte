init -1 python:
    nvl_fontsize = 48
    nvl_fontfamily = "fonts/Rubik.ttf"
    color_chatname = "#8D727A"
    color_chatnarrator = "#988188"
    color_choicetext = "#8D727A"
    message_space = 20
    ChatSystem_ChatName = "CHAT"
    ChatSystem_ChatBGIM = "chat/phone_background.png"
    def SFX_ChatSystem(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/typewriter-soft-click.mp3", relative_volume=0.2)
    def nvl_to_adv_but_keep_nvl(mode, old_modes):
        if mode == 'say' or mode == 'menu':
            widget_properties, dialogue, show_args = _m1_00nvl_mode__nvl_screen_dialogue()
            if dialogue:
                renpy.show_screen('nvl', _layer=config.nvl_layer, _widget_properties=widget_properties, dialogue=dialogue, **show_args)
    config.mode_callbacks.append(nvl_to_adv_but_keep_nvl)



transform t_chat_message():
    # subpixel True
    alpha 0.0
    yoffset 50
    parallel:
        ease 0.2 alpha 1.0
    parallel:
        easein_circ 0.4 yoffset 0
transform t_chat_narrator():
    # subpixel True
    alpha 0.0
    ease 0.5 alpha 1.0
transform t_chat_phone():
    # subpixel True
    # alpha 0.0
    yoffset 1080
    # parallel:
    #     ease 0.5 alpha 1.0
    parallel:
        easein_circ v_TransitionTime yoffset 0
transform uuuuuu_phone:
    subpixel True
    anchor 0
transform dddddd_phone:
    subpixel True
    yanchor -1200
define t_ChatSystem = MoveTransition(
    v_TransitionTime, enter=uuuuuu_phone,leave=dddddd_phone,layers=['screens'],
    time_warp=_warper.easein_circ,enter_time_warp=_warper.easein_circ,leave_time_warp=_warper.easein_circ
)



screen Chat_MessageBox(dwhat, dwhat_id, chat_bubble_color, chat_text_color):
    frame:
        background AlphaMask(Solid(chat_bubble_color), Frame("chat/phone_chat_bubble.png", 24,24,24,24))
        padding (40,30,40,38)
        xsize 750
        text dwhat:
            xsize 665
            font nvl_fontfamily
            color chat_text_color
            size nvl_fontsize
            xalign 0.0
            yalign 0.0
            slow_cps False
            id dwhat_id



screen ChatSystem(dialogue, items=[]):
    frame:
        if len(dialogue) == 1:
            at t_chat_phone
        # background Solid("#273f66")
        background Transform(ChatSystem_ChatBGIM, xcenter=0.5,yalign=0.5)
        foreground Transform("chat/phone_foreground.png", xcenter=0.5,yalign=0.5)
        xsize 920
        ysize 860
        xalign 0.5
        yalign 0.5
        viewport:
            draggable True
            mousewheel True
            xinitial 0.0
            yinitial 1.0
            # scrollbars "all"
            vbox:
                spacing 20
                $ previous_d_who = None
                for id_d, d in enumerate(dialogue):
                    # Narrator
                    if d.who == None:
                        if d.what != "":
                            null height message_space
                            text d.what:
                                if d.current and len(items)==0 and renpy.get_mode()=="nvl":
                                    at t_chat_narrator
                                font nvl_fontfamily
                                size nvl_fontsize
                                color color_chatnarrator
                                xsize 850
                                xpos -135
                                text_align 0.5
                                italic True
                                slow_cps False
                                id d.what_id
                        else:
                            text d.what:
                                id d.what_id
                                font nvl_fontfamily
                                size 0
                    # Characters
                    else:
                        if previous_d_who != d.who:
                            null height message_space
                            hbox:
                                if d.current and len(items)==0 and renpy.get_mode()=="nvl":
                                    at t_chat_message
                                spacing 25
                                add d.who_args['chat_avatar']
                                vbox:
                                    spacing 20
                                    text d.who:
                                        size nvl_fontsize
                                        font nvl_fontfamily
                                        color d.who_args['chat_name_color']
                                    use Chat_MessageBox(d.what, d.what_id, d.who_args['chat_bubble_color'], d.who_args['chat_text_color'])
                        else:
                            hbox:
                                if d.current and len(items)==0 and renpy.get_mode()=="nvl":
                                    at t_chat_message
                                spacing 25
                                null width 80 # The width of the avatar
                                vbox:
                                    use Chat_MessageBox(d.what, d.what_id, d.who_args['chat_bubble_color'], d.who_args['chat_text_color'])

                    $ previous_d_who = d.who
                # NVL Menu
                if len(items) > 0:
                    null height message_space
                    for menu_choice in items:
                        button:
                            if renpy.get_mode()=="nvl":
                                at t_chat_message
                            action menu_choice.action
                            frame:
                                background Frame("chat/phone_menu_choice.png", 24,24,24,24)
                                hover_background Frame("chat/phone_menu_choice_hover.png", 24,24,24,24)
                                padding (24,48)
                                xsize 850
                                ysize 120
                                xpos 25
                                text menu_choice.caption:
                                    size nvl_fontsize
                                    font nvl_fontfamily
                                    color color_choicetext
                                    text_align 0.5
                                    xalign 0.5
                                    yalign 0.5
                
                null height 60

    text ChatSystem_ChatName:
        if len(dialogue) == 1:
            at t_chat_phone
        yoffset -480
        xalign 0.5
        yalign 0.5
        size nvl_fontsize
        font nvl_fontfamily
        color color_chatname
