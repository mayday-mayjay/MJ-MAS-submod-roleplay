init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="MJroleplay_intro",
            aff_range=(mas_aff.NORMAL, None),
            action=EV_ACT_RANDOM
            random=True
        )
    )

label MJroleplay_intro:
  m "[player], are you familiar with Dungeons and Dragons?"
  extend "DnD, for short."
  m ""
  return "no_unlock|derandom"
