init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="MJroleplay_start",
            category=["Roleplay"],
            prompt="I wanna do some DND-style roleplay!",
            conditional="seen_event('MJroleplay_intro')",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.NORMAL, None),
            pool=True,
            unlocked=False
        )
    )

label MJroleplay_start:
    m "Really, [player]?"
    extend "Yay! Let's do this!"
    m ""
    return
