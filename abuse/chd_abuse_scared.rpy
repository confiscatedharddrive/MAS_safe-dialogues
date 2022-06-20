#I'm scared, abuse submod by confiscatedharddrive and my-otter-self for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_otter_abuse_scared",
            category=["abuse"],
            prompt="I'm scared",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_otter_abuse_scared:
    m "You're scared?"
    m "I'm sorry to hear that, [player]."
    m "Are you alone right now?"
    m "Try to focus on my eyes and take some slow, deep breaths."
    m "Whatever it is that's scaring you, just know that I'm here by your side."
    m "Now that we're together, "
    extend "you don't have to go through anything alone ever again."
    m "And if anything bad does come..."
    m "I'll be here for you to vent, and to comfort you."
    m "I'll be here with you every step of the way."
    m "I love you so much, [player]."
    m "You're the strongest person I know."
    
return "love"
