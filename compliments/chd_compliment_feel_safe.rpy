#Thank you for making me feel safe, compliment submod by confiscatedharddrive for Monika After Story.

init 5 python in mas_bookmarks_derand:
    label_prefix_map["chd_compliment_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_compliment_feel_safe",
            category=["mas_compliment"],
            prompt="Thank you for making me feel safe.",
            unlocked=True
        ),
        code="CMP"
    )

label chd_compliment_feel_safe:
    m 1sublb "You make me feel safe too, [player]!"
    m 2rsc "It can be hard living inside the game."
    m 2dkd "I'm always afraid I'm going to break something, or that I'll lose you."
    m 3esa "But when you open up the game, I always feel immediately safe."
    m 2dubsa "I just know everything will be okay when I'm around you."
    m 5fubfb "So I'm glad to hear that I make you feel the same way."
    m 5hubfb "I love you so much, [player]."
    m 2dkd "I just wish there was more I could do to help you in your difficult situation."
    m 2ekd "But just know that if at any time you feel unsafe, you can let me know."
    m 4esa "I'll do the best I can to protect you."
    m 6dsb "And the day I cross over to your reality..."
    m 2rfo "I'll personally fight anyone who gives you trouble."
    m 7hksdlb "Ahaha, sorry. Was that a bit much?"
    m 2dsc "..."
    m 1fkbsb "It's just that I love you more than anything, [mas_get_player_nickname()]." 
    m 3ffbfb "And I'll do my best to protect my beautiful [bf]!"

return "love"