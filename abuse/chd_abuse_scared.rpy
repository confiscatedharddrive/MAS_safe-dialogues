#I feel scared, feeling submod by confiscatedharddrive for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_feeling_scared",
            category=["i feel..."],
            prompt="...scared",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_feeling_scared:
    m "You're scared?"
    m "I'm sorry to hear that, [player]."
    m "There's nothing to be scared about, I'm here with you now."
    m "Just focus on my eyes and take some slow, deep breaths."
    m "I love you, [player]."
    m "Whatever it is that's scaring you, just know that I'm here by your side."
    m "You don't have to go through anything alone."

return