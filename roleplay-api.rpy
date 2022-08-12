default persistent._dj_rpg_stories_db = dict()
default persistent._dj_rpg_abandoned = set()
default persistent._dj_rpg_done = set()

init 5 python:
    _dj_rpg_stories_db = dict()
    mas_all_ev_db_map["DJ_STR"] = _dj_rpg_stories_db

init 10 python:
    def dj_markAbandoned(ev=None):
        if ev is None:
            ev = mas_getEV(mas_globals.this_ev)
        if type(ev) is unicode:
            ev = mas_getEV(ev)

        persistent._dj_rpg_abandoned.add(ev.eventlabel)

    def dj_markDone(ev=None):
        if ev is None:
            ev = mas_getEV(mas_globals.this_ev)
        if type(ev) is unicode:
            ev = mas_getEV(ev)

        persistent._dj_rpg_done.add(ev.eventlabel)
