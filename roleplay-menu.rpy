# adjustments for the twopane menu
define dj_prev_adj = ui.adjustment()
define dj_main_adj = ui.adjustment()

#scrollable_menu selection screen
#This screen is based on work from the tutorial menu selection by haloff1
screen dj_twopane_scrollable_menu(prev_items, main_items, left_area, left_align, right_area, right_align, cat_length):
    on "hide" action Function(store.dj_main_adj.change, 0)

    default flt_evs = None

    style_prefix "twopane_scrollable_menu"

    # If the user used search, we show only teh results
    if flt_evs is not None:
        fixed:
            pos (left_area[0], left_area[1])
            xsize right_area[0] - left_area[0] + right_area[2]
            ysize left_area[3]

            vbox:
                pos (0, 0)
                anchor (0, 0)

                viewport:
                    id "viewport"
                    yfill False
                    mousewheel True
                    arrowkeys True

                    vbox:
                        for ev in flt_evs:
                            textbutton ev.prompt:
                                if renpy.has_label(ev.eventlabel) and not seen_event(ev.eventlabel):
                                    style "scrollable_menu_new_button"
                                else:
                                    style "scrollable_menu_button"
                                xsize right_area[0] - left_area[0] + right_area[2]
                                action [Function(mas_ui.twopane_menu_delegate_callback, ev.eventlabel), Return(ev.eventlabel)]

                null height 20

                textbutton _("Nevermind."):
                    style "scrollable_menu_button"
                    xsize right_area[0] - left_area[0] + right_area[2]
                    action [Return(False), Function(store.dj_prev_adj.change, 0)]

            bar:
                style "classroom_vscrollbar"
                value YScrollValue("viewport")
                # RenPy is tresh, so we have to do this here
                xalign left_align / 2 + 0.005

    # Otherwise basic twopane
    else:
        # Left panel
        fixed:
            anchor (0, 0)
            pos (left_area[0], left_area[1])
            xsize left_area[2]

            if cat_length != 1:
                ysize left_area[3]
            else:
                ysize left_area[3] + evhand.LEFT_EXTRA_SPACE

            bar:
                adjustment dj_prev_adj
                style "classroom_vscrollbar"
                xalign left_align

            vbox:
                ypos 0
                yanchor 0

                viewport:
                    yadjustment dj_prev_adj
                    yfill False
                    mousewheel True
                    arrowkeys True

                    vbox:
                        for i_caption, i_label in prev_items:
                            textbutton i_caption:
                                if renpy.has_label(i_label) and not seen_event(i_label):
                                    style "twopane_scrollable_menu_new_button"

                                elif not renpy.has_label(i_label):
                                    style "twopane_scrollable_menu_special_button"

                                action Return(i_label)

                if cat_length != 1:
                    null height 20

                    if cat_length == 0:
                        textbutton _("Nevermind.") action [Return(False), Function(store.dj_prev_adj.change, 0)]

                    elif cat_length > 1:
                        textbutton _("Go Back") action [Return(-1), Function(store.dj_prev_adj.change, 0)]

        # Right panel
        if main_items:
            fixed:
                area right_area

                bar:
                    adjustment dj_main_adj
                    style "classroom_vscrollbar"
                    xalign right_align

                vbox:
                    ypos 0
                    yanchor 0

                    viewport:
                        yadjustment dj_main_adj
                        yfill False
                        mousewheel True
                        arrowkeys True

                        vbox:
                            for i_caption, i_label in main_items:
                                textbutton i_caption:
                                    if renpy.has_label(i_label) and not seen_event(i_label):
                                        style "twopane_scrollable_menu_new_button"

                                    elif not renpy.has_label(i_label):
                                        style "twopane_scrollable_menu_special_button"

                                    action [Return(i_label), Function(store.dj_prev_adj.change, 0)]

                    null height 20

                    textbutton _("Nevermind.") action [Return(False), Function(store.dj_prev_adj.change, 0)]

    # Search bar
    # The constants are hardcoded, but the menu looks good so just don't change them
    frame:
        xpos left_area[0]
        ypos left_area[1] - 55
        xsize right_area[0] - left_area[0] + right_area[2]# 530
        ysize 40
        background Solid("#ffaa99aa")

        viewport:
            draggable False
            arrowkeys False
            mousewheel "horizontal"
            xsize right_area[0] - left_area[0] + right_area[2] - 10
            ysize 38
            xadjustment ui.adjustment(ranged=store.mas_ui.dj_twopane_menu_adj_ranged_callback)

            input:
                id "search_input"
                style_prefix "input"
                length 50
                xalign 0.0
                layout "nobreak"
                first_indent (0 if flt_evs is None else 10)
                changed store.mas_ui.dj_twopane_menu_search_callback

        if flt_evs is None:
            text "Search for a story...":
                text_align 0.0
                layout "nobreak"
                color "#EEEEEEB2"
                first_indent 10
                line_leading 1
                outlines []

init 10 python in mas_ui:
    _DJ_TWOPANE_MENU_MAX_FLT_ITEMS = 50
    _DJ_TWOPANE_MENU_SEARCH_DBS = store.mas_all_ev_db_map["DJ_STR"].values()
    _DJ_TWOPANE_MENU_DELEGATES_CALLBACK_MAP = dict()

    def _dj_twopane_menu_sort_events(ev, search_query, search_kws):
        """
        The sortkey for events in the twopane menu.
        IN:
            ev - event object
            search_query - search query to sort by
            search_kws - search_query splitted using spaces
        OUT:
            weight as int
        """
        ev_prompt = ev.prompt.lower()
        ev_label = ev.eventlabel.lower()
        ev_cat_full = " ".join(map(str, ev.category)) if ev.category else ""

        weight = 0
        base_increment = 2
        base_modifier = len(search_kws) + 1

        if search_query == ev_prompt or search_query == ev_label:
            weight += base_increment * base_modifier**8

        elif search_query in ev_prompt:
            if ev_prompt.startswith(search_query):
                weight += base_increment * base_modifier**7

            else:
                weight += base_increment * base_modifier**6

        elif search_query in ev_label:
            if ev_label.startswith(search_query):
                weight += base_increment * base_modifier**5

            else:
                weight += base_increment * base_modifier**4

        else:
            for search_kw in search_kws:
                if search_kw in ev_prompt:
                    weight += base_increment * base_modifier**3

                elif search_kw in ev_label:
                    weight += base_increment * base_modifier**2

                elif ev_cat_full:
                    if search_kw in ev.category:
                        weight += base_increment * base_modifier

                    elif search_kw in ev_cat_full:
                        weight += base_increment

        return weight

    def _dj_twopane_menu_filter_events(ev, search_query, search_kws):
        """
        The filter for events in the twopane menu
        IN:
            ev - event object
            search_query - search query to filter by
            search_kws - search_query splitted using spaces
        OUT:
            boolean whether or not the event pass the criteria
        """
        ev_prompt = ev.prompt.lower()
        ev_label = ev.eventlabel.lower()
        ev_cat_full = " ".join(map(str, ev.category)) if ev.category else ""

        # First, basic filters so we only deal with appropriate events
        if ev_prompt == ev_label:
            return False

        if not ev.unlocked:
            return False

        if ev.anyflags(store.EV_FLAG_HFNAS):
            return False

        if not ev.checkAffection(store.mas_curr_affection):
            return False

        if not ev.checkConditional():
            return False

        if not search_query:
            return True

        # This is so we can interrup the loop early
        for search_kw in search_kws:
            if (
                search_kw in ev_prompt
                or search_kw in ev_label
                or (ev_cat_full and search_kw in ev_cat_full)
            ):
                return True

        return False

    def _dj_twopane_menu_search_events(search_query):
        """
        The actual method that does filtering and searching for the twopane menu.
        NOTE: won't return more than TWOPANE_MENU_MAX_FLT_ITEMS events
        IN:
            search_query - search query to filter and sort by
        OUT:
            list of event objects or None if empty query was given
        """
        if not search_query:
            return None

        search_query = search_query.lower()
        search_query = search_query.strip()
        search_kws = search_query.split()

        flt_evs = [
            ev
            for ev in _DJ_TWOPANE_MENU_SEARCH_DBS
            if _dj_twopane_menu_filter_events(ev, search_query, search_kws)
        ]
        flt_evs.sort(key=lambda ev: _dj_twopane_menu_sort_events(ev, search_query, search_kws), reverse=True)

        return flt_evs[0:_DJ_TWOPANE_MENU_MAX_FLT_ITEMS]

    def dj_twopane_menu_adj_ranged_callback(adj):
        """
        This is called by an adjustment of the twopane menu
        when its range is being changed (set)
        IN:
            adj - the adj object
        """
        widget = renpy.get_widget("dj_twopane_menu_adj_ranged_callback", "search_input", "screens")
        caret_relative_pos = 1.0
        if widget is not None:
            caret_pos = widget.caret_pos
            content_len = len(widget.content)

            if content_len > 0:
                caret_relative_pos = caret_pos / float(content_len)

        # This ensures that the caret is always visible (close enough) to the user
        # when they enter text
        adj.change(adj.range * caret_relative_pos)

    def dj_twopane_menu_search_callback(search_query):
        """
        The callback the input calls when the user enters anything.
        Updates flt_evs of the twopane menu and causes RenPy to update the screen.
        IN:
            search_query - search query to filter and sort by
        """
        # Get the screen to pass events into
        scr = renpy.get_screen("dj_twopane_scrollable_menu")
        if scr is not None:
            # Search
            scr.scope["flt_evs"] = _dj_twopane_menu_search_events(search_query)
        # Update the screen
        renpy.restart_interaction()

    def dj_twopane_menu_delegate_callback(ev_label):
        """
        A method to handle delegate logic for some of our events
        when the user skips a delegate label using search
        NOTE: the callback will be called before we push the event
        TODO: add more callbacks as needed
        IN:
            ev_label - the ev_label of the event the user's selected
        """
        for prefix in _DJ_TWOPANE_MENU_DELEGATES_CALLBACK_MAP:
            if ev_label.startswith(prefix):
                _DJ_TWOPANE_MENU_DELEGATES_CALLBACK_MAP[prefix]()
                return
        return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="rpgMod_menu",
            prompt="I want to come back to some story...",
            category=["roleplaying"],
            pool=True,
            rules={"no_unlock": None}
        ),
        code="EVE"
    )

label rpgMod_menu:
    python:
        import store.evhand as evhand

        dj_prev_items = (
            ("In Progress", "progress"),
            ("Abandoned", "abandon"),
            ("Done", "done")
        )
        dj_current_category = None
        dj_main_items = None

        dj_picked_event = False

    while not dj_picked_event:
        if dj_current_category is not None:
            python:
                dj_events = Event.filterEvents(
                    mas_all_ev_db_map["DJ_STR"],
                    unlocked=True,
                    aff=mas_curr_affection,
                    flag_ban=EV_FLAG_HFM
                )

                if dj_current_category == "progress":
                    for key in dj_events.keys():
                        if key in persistent._dj_rpg_abandoned or key in persistent._dj_rpg_done:
                            del dj_events[key]
                elif dj_current_category == "abandon":
                    for key in dj_events.keys():
                        if key not in persistent._dj_rpg_abandoned:
                            del dj_events[key]
                elif dj_current_category == "done":
                    for key in dj_events.keys():
                        if key not in persistent._dj_rpg_done:
                            del dj_events[key]
                dj_main_items = list(map(lambda e: (e.prompt, e.eventlabel), dj_events.values()))
        else:
            $ dj_main_items = None

        call screen dj_twopane_scrollable_menu(dj_prev_items, dj_main_items, evhand.LEFT_AREA, evhand.LEFT_XALIGN, evhand.RIGHT_AREA, evhand.RIGHT_XALIGN, 1 if dj_current_category is not None else 0) nopredict
        if _return in dict(dj_prev_items).values():
            $ dj_current_category = filter(lambda e: e[1] == _return, dj_prev_items)[0]
        elif _return == -1:
            $ dj_current_category = None
        else:
            $ dj_picked_event = True
            if _return is not False:
                $ mas_setEventPause(None)
                $ pushEvent(_return, skipeval=True)

    return