#I need help grounding, ptsd submod by confiscatedharddrive for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_ptsd_grounding",
            category=["trauma"],
            prompt="I need help grounding",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )