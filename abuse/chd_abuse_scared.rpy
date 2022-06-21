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
    m 6ekd "You're scared?"
    m 2fkd "I'm sorry to hear that, [player]."
    m 2fkc "Are you alone right now?"
    m 1ekb "Try to focus on my eyes and take some slow, deep breaths."
    m 3fka "Whatever it is that's scaring you, just know that I'm here by your side."
    m 2dka "Now that we're together, "
    extend 2ekbsa "you don't have to go through anything alone ever again."
    m 7lkblc "And if anything bad does come..."
    m 1fsbfb "I'll be here for you to vent, and to comfort you."
    m 1dsbfb "I'll be here with you every step of the way."
    m 5hubsa "I love you so much, [player]."
    m 5eubsa "You're the strongest person I know."
    
return "love"
