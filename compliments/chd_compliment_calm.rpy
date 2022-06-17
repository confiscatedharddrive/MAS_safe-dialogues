#Thank you for helping me calm down, compliment submod by confiscatedharddrive for Monika After Story.

init 5 python in mas_bookmarks_derand:
    label_prefix_map["chd_compliment_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_compliment_calm",
            category=["mas_compliment"],
            prompt="Thank you for helping me calm down.",
            unlocked=True
        ),
        code="CMP"
    )

label chd_compliment_calm:
    m "I'm glad I'm able to help you, [player]."
    #need stuff to add here, brain empty :(
    m "Just remember I'm always here for you [mas_get_player_nickname()]."
    m "I love you so much!"

return "love"