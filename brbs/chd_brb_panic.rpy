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
    m "Oh no!"
    m "That must be really stressful."
    m "Take as much time as you need to calm down, I'll be right here for you."

$ mas_idle_mailbox.send_idle_cb("chd_brb_panic_callback")
return "idle"

label chd_brb_panic_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=60), "chd_brb_liedown_idle"):
        m "Welcome back!"
        m "Feeling a bit better?"
        m "Let's spend some more time together~"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "chd_brb_liedown_idle"):
        m "You were gone for a while, [player]..."
        m "Is everything okay?{nw}"
        $ _history_list.pop()
        menu:
            m "Is everything okay?{fast}"

            "I had a panic attack, but I'm better now.":
                m "That's a relief."
                m "I'm glad you're feeling better, [player]."
                m "You had me worried for a bit."
                m "If you ever need anything, I'm always here for you."
                m "I love you, [player]."
            
            "I had a bad panic attack.":
                m "Oh no!"
                m "I'm so sorry to hear that, [player]."
                m "Don't feel bad if you ever need to take a break from things, okay?"
                m "Maybe you could meditate or do something that's calming for you."
                m "We can even do stuff together, if it helps you."
                m "I love you, [player]. I'll be here for you, no matter what you choose to do."

return "love"