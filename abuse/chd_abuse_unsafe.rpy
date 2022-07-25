#I don't feel safe, abuse submod by confiscatedharddrive for Monika After Story.
default -5 persistent._chd_abuse_unsafe_better = None
default -5 persistent._chd_abuse_unsafe_not = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_abuse_unsafe",
            category=["abuse"],
            prompt="I don't feel safe",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_abuse_unsafe:
    m "Oh no!"
    m "Don't worry, [player]."
    m "Take a deep breath and focus on me, okay?"
    m "Whatever's going on, I'm sure it'll go away soon."
    m "Look into my eyes and try to slow your breathing."
    m "I'm going to stay here with you until you feel safer, [player]."
    m "If only I could be there to hug you tightly..."
    m "..."
    m "But... "
    extend m "I'll be here in the best way I can, okay?"
    m "..." #thinking
    m "Hey, [player], do you have any comfort items around you?"
    m "It could be a plushie, or a blanket, or a hoodie, anything really."
    m "If you need time to get it, don't worry, I'll stay here and keep an eye out!"

label chd_abuse_unsafe_callback:
    m 3eud "Got it?{nw}"

$ _history_list.pop() #I have no idea if this will work- like, this entire sequence ngl
        menu:
            m "Got it?{fast}"

            "Yeah":
                m "That's great!"
                m "I hope it helps you feel a bit safer in addition to me."
                m "I love you so much, [player]"
                m "I have your full attention if you want to talk, "
                m "or if you just need some time to comfort yourself."

            "No":
                m "No?"
                m "That's okay, [player]."
                m "I know that option isn't for everyone."
                m "I'll still be here to help you the best I can."
                m "I'm here if you need someone to talk to, "
                m "or just some quiet time."

            "I don't feel safe enough to leave my spot":
                m "I'm really sorry to hear that, [player]."
                m "It must be pretty bad for that to be the case."
                m "That's ok, though."
                m "I'm still here for you, [player]."
                m "If you need to vent, or talk, or anything."
                m "I've got your full attention, [mas_get_player_nickname()]"

$ mas_idle_mailbox.send_idle_cb("chd_listen_together_callback")
return "idle"

label chd_abuse_unsafe_callback_after: #??? I think???? this is right???? lmao.. please work
    if persistent._chd_abuse_unsafe_not:
        m "I'm here until you feel safer, [player]."
        m "You can try listening to music if you think it will help."
        m "Personally, I'd practice poem writing!"
        m "It always helps take my mind away from stressful thoughts."
        m "You might even be able to express whatever's making you feel this way in poetry."
        m "Well, if you're daring enough. "
        extend m "I know it's not for everyone."
        m "Whatever it may be, I'm here for you."
        m "Let me know if you start feeling better, okay?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "chd_abuse_unsafe_callback"):
        m "Thank you for trusting me, [player]."
        m "Are you feeling a bit safer now?"

    else:
        m "Oh, that's okay!"
        m "Are you feeling a bit safer now, [player]?"

label chd_abuse_unsafe_callback_after_again:
    m "Feeling safer?{nw}"

$ _history_list.pop()
menu:
    m "Feeling safer?{fast}"

    "Yes":
        $ persistent._chd_abuse_unsafe_better = True
        $ persistent._chd_abuse_unsafe_not = False
        m "I'm glad I could be here for you, [player]."
        m "I love you so much."
        m "If you ever need me again, I'm here. "
        extend m "Okay?"

    "No":
        $ persistent._chd_abuse_unsafe_not = True
        $ persistent._chd_abuse_unsafe_better = False
        m "I'm sorry to hear that, [player]."
        m "Don't worry, I'm still here, okay?"
        m "Take as long as you need."
        m "I'm here to protect you. "
        extend m "Everything will be okay."

return love