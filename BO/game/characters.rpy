# ====================================================================================================

# ---------- Default Narrator ----------
define narrator = Character(
    callback=SFX_Dialogue,
    ctc="CTC", ctc_position="fixed",
)

# ====================================================================================================

# ---------- Character Baek Dohyun ----------
# Normal dialogue
define baek = Character(
    "Baek Dohyun",
    callback=SFX_Dialogue,
    color="#98C0CD",
    ctc="CTC", ctc_position="fixed",
)
# Chat dialogue
define baek_chat = Character(
    "Baek Dohyun",
    kind=nvl, 
    callback=SFX_ChatSystem,
    chat_bubble_color="#75ABBD",
    chat_name_color="#75ABBD",
    chat_text_color="#FFFFFF",
    chat_avatar="avatar_baekdohyun.png",
)

# ====================================================================================================

# ---------- Character Jang Haein ----------
# Normal dialogue
define jang = Character(
    "Jang Haein",
    callback=SFX_Dialogue,
    color="#DFBA9F",
    ctc="CTC", ctc_position="fixed",
)
# Chat dialogue
define jang_chat = Character(
    "Jang Haein",
    kind=nvl, 
    callback=SFX_ChatSystem,
    chat_bubble_color="#E7A474",
    chat_name_color="#E7A474",
    chat_text_color="#FFFFFF",
    chat_avatar="avatar_janghaein.png",
)

# ====================================================================================================

# ---------- Character Prof. Lee ----------
# Chat dialogue
define prof_chat = Character(
    "Prof. Lee",
    kind=nvl,
    callback=SFX_ChatSystem,
    chat_bubble_color="#917d83",
    chat_name_color="#917d83",
    chat_text_color="#FFFFFF",
    chat_avatar="avatar_unknown.png",
)

# ====================================================================================================