from items import *

room_reception={
    "name" : "Reception",
	
    "description":
    """    As you walk into reception you see bolted doors sealed with rusty bars plastered with "DO NOT ENTER" signs from the outside. 
    You can see bloody handprints against the locked doors, pools of blood swimming with empty shells infront of them. 
    There is a newspaper sat on the receptionist desk the only thing left not broken, kicked in or dripping in blood. 
    The newspaper could explain what has happened to the town.
    You hear footsteps from upstairs and splitting screams from distances outside.
    """,

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_newspaper, item_handbook]
}

room_admins = {
    "name": "MJ and Simon's room",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits":  {"north": "Reception"},

    "items": []
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"west": "Reception"},

    "items": []
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": []
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Parking"},

    "items": [item_pen]
}



rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}
