from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user","menu","choose_type","introduction","type1","type2","type3","type4","cancel"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "choose_type",
                "dest": "type1",
                "conditions": "is_going_to_type1",
            },
            {
                "trigger": "advance",
                "source": "choose_type",
                "dest": "type2",
                "conditions": "is_going_to_type2",
            },
            {
                "trigger": "advance",
                "source": "choose_type",
                "dest": "type3",
                "conditions": "is_going_to_type3",
            },
            {
                "trigger": "advance",
                "source": "choose_type",
                "dest": "type4",
                "conditions": "is_going_to_type4",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "choose_type",
                "conditions": "is_going_to_choose_type",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "introduction",
                "conditions": "is_going_to_introduction",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "introduction",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": ["type1","type2","type3","type4"],
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "choose_type",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": ["type1","type2","type3","type4"],
                "dest": "choose_type",
                "conditions": "is_going_to_choose_type",
            },
            {"trigger": "go_back", "source": ["cancel","introduction","choose_type","type1","type2","type3","type4"], "dest": "user"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine