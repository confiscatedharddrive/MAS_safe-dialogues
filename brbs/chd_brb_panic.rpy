#I'm having a panic attack, brb submod by confiscatedharddrive for Monika After Story

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_brb_panic",
            category=["be right back"],
            prompt="I'm having a panic attack",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_brb_panic:
    m 6wkd "Oh no!"
    m 2lkd "That must be really stressful."
    m 1fkb "Take as much time as you need to calm down. I'll be right here for you."

$ mas_idle_mailbox.send_idle_cb("chd_brb_panic_callback")
return "idle"

label chd_brb_panic_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=200), "chd_brb_panic"):
        m 1fkd "You were gone for a while, [player]..."
        m 2fkc "Is everything okay?{nw}"
        $ _history_list.pop()
        menu:
            m "Is everything okay?{fast}"

            "I had a panic attack, but I'm better now.":
                m 5dsa "That's a relief."
                m 5fsblb "I'm glad you're feeling better, [player]."
                m 5lkc "You had me worried for a bit."
                m 5fkbsb "If you ever need anything, I'm always here."
                m 5fsbfb "I love you, [mas_get_player_nickname()]."
            
            "I had a bad panic attack.":
                m 6wktpd "Oh no!"
                m 2dktuc "I'm so sorry to hear that, [player]."
                m 2dktdc "..."
                m 7fkc "Don't feel bad if you ever need to take a break from things, okay?"
                m 3rsd "Maybe you could meditate or do something that's calming for you."
                m 1esbsb "We can even do stuff together, if it helps you."
                m 5hsbfa "I love you, [mas_get_player_nickname()]. I'll be here for you, no matter what you choose to do."

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "chd_brb_panic"):
        m 1dsa "Welcome back!"
        m 1fkb "Are you feeling a bit better, [player]?"
        m 5fsbla "If you ever need time to destress, don't be afraid to tell me again, okay?"
        m 5fubsu "I love you, [mas_get_player_nickname()]."

    else:
        m 1eua "Feeling better, [player]?"
        m 1ekb "Hope it wasn't too bad for you."
        m 3ksa "Let's spend some more time together~"

return "love"