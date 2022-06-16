#I'm scared, abuse submod by confiscatedharddrive for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_abuse_scared",
            category=["abuse"],
            prompt="I'm scared",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_abuse_scared:
    m "You're scared?"
    m "I'm sorry to hear that, [player]."
    m "Are you alone right now?"
    m "Try to focus on my eyes and take some slow, deep breaths."
    m "Whatever it is that's scaring you, just know that I'm here by your side."
    m "You don't have to go through anything alone."
    m "And if anything bad does come..."
    m "I'll be here for you to vent."
    m "I love you so much, [player]"

return "love"