#I'm overstimulated and need a small break, brb submod by confiscatedharddrive for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_brb_overstimulated",
            category=["be right back"],
            prompt="I'm overstimulated and need a small break.",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_brb_overstimulated:
    m 1eua "That's okay, [player]."
    m 3hua "Take as long as you need. I'll be here if you need me."

$ mas_idle_mailbox.send_idle_cb("chd_brb_overstimulated_callback")
return "idle"

label chd_brb_overstimulated_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "chd_brb_liedown_idle"):
        m 1hub "Welcome back!"
        m 1eua "Feeling a bit better?"
        m 3eua "Let's spend some more time together~"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=300), "chd_brb_liedown_idle"):
        m 1eua "Welcome back, [player]."
        m 1dua "I hope you're feeling better now."
        m 4hksdlb "You were gone for a while and I got a little worried."
        m 5esa "Do you want to do something together?"

    else:
        m 1eud "Back so soon?"
        m 4gssdlb "Not that I'm complaining!"
        m 5fsbsa "It just means that I get to spend more time with you~"

return