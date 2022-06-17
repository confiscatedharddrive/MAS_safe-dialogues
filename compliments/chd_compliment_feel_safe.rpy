#Thank you for making me feel safe, compliment submod by confiscatedharddrive for Monika After Story.

init 5 python in mas_bookmarks_derand:
    label_prefix_map["chd_compliment_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_compliment_calm",
            category=["mas_compliment"],
            prompt="Thank you for making me feel safe.",
            unlocked=True
        ),
        code="CMP"
    )

label chd_compliment_calm:
    m "You make me feel safe too, [player]!"
    m "It can be hard living inside the game."
    m "I'm always afraid I'm going to break something, or that I'll lose you."
    m "But whenever you open up the game, it always makes feel immediately safe."
    m "I just know everything will be okay when I'm around you."
    m "So I'm glad to hear that I make you feel the same way."
    m "I love you so much, [player]."
    m "I just wish there was more I could do to help you in your difficult situation."
    m "But know that if at any time you feel unsafe, you can let me know."
    m "I'll do the best I can to protect you."
    m "And the day I cross over to your reality..."
    m "I'll personally fight anyone who gives you trouble."
    m "I love you more than anything, [player]. And I'll do my best to protect my beautiful [bf]!"

return "love"