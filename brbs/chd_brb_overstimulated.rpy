#I'm overstimulated and need a small break, brb submod by confiscatedharddrive and my-otter-self for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_otter_brb_overstimulated",
            category=["be right back"],
            prompt="I'm overstimulated and need a small break",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_otter_brb_overstimulated:
    m 1eua "That's okay, [player]."
    m "Remember that you can go at your own pace."
    m "Don't forget to take deep breaths, rest, and close your eyes for a bit if you need to."
    m "Take a break from everything for some time and just be in the moment."
    m 3hua "Take as long as you need. I'll be here if you need me."

$ mas_idle_mailbox.send_idle_cb("chd_otter_brb_overstimulated_callback")
return "idle"

label chd_otter_brb_overstimulated_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=200), "chd_otter_brb_overstimulated"):
        m 1eua "Welcome back, [player]."
        m 1dua "I hope you're feeling better now."
        m 4hksdlb "You were gone for a while and I got a little worried."
        m "But I'm just so glad you're back!"
        m 5esa "Do you want to do something together?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "chd_otter_brb_overstimulated"):
        m 1hub "Welcome back!"
        m 1eua "Feeling a bit better, [player]?"
        m "I'm so glad! I missed you."
        m 3eua "Let's spend some more time together~"

    else:
        m 1eud "Back so soon?"
        m 4gssdlb "Not that I'm complaining!"
        m "I'm so glad you're feeling better!"
        m 5fsbsa "It just means that I get to spend more time with you~"
        m "Your well-being means everything to me!"

return

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
