item_newspaper = {
    "id": "newspaper",

    "name": "A newspaper",

    "recipe": [],

    "damage": 0,

    "energy": 0,

    "description": 

    """HEADLINE: HYSTERIA IN THE HOSPITAL """

}

item_pen = {
    "id": "pen",
    
    "name": "A pen",

    "recipe": [],

    "damage": 1,

    "energy": 0,

    "description": "A basic ballpoint pen."
}


item_patients_gown = {
    "id": "gown",
    
    "name": "A patients gown",

    "recipe": [],

    "damage": 0,

    "energy": 0,

    "description": "A basic patients gown to keep you warm."
}

item_card = {
    "id": "card",
    
    "name": "A get well soon card",

    "recipe": [],

    "damage": 0,

    "energy": 0,

    "description": "A get well soon card written to you by your family."
}

item_bedsheet = {
    "id": "bedsheet",

    "name": "Surgical bedsheets",

    "recipe": [],

    "damage": 0,

    "energy": 0,

    "description": "A pile of bloody bedsheets."
}

item_suture = {
    "id": "suture",

    "name": "Surgical suture kit",

    "recipe": [],

    "damage": 3,

    "energy": 0,

    "description": "the kit contains: surgical needles, nylon sutures (thread), scalpel, small scissors, tape."
}

item_rope = {
    "id": "rope",

    "name": "A pile of rope",

    "recipe": [],

    "damage": 2,

    "energy": 0,

    "description": "a thick, dusty rope probably left over from the renovation of the hospital."
}

item_gun = {
    "id":"gun",

    "name": "A classic pistol",

    "recipe": [],

    "damage": 4,

    "energy": 0,

    "description": "oh no! there are no bullets in the pistol, maybe there are lying around somewhere else..."
}

item_bullets = {
    "id": "bullets",

    "name": "bunch of bullets",

    "recipe": [],

    "damage": 1,

    "energy": 0,

    "description": "a bunch of bullets scattered on the floor, there must be a gun around somewhere..."
}

item_loadedgun = {
    
    "id":"gun_loaded",

    "name": "A classic pistol, loaded",

    "recipe": [item_gun, item_bullets],

    "damage": 10,

    "energy": 0,

    "description": "Shiny and deadly"
}

item_xrayNote = {
    "id": "notes",

    "name": "research notes",

    "recipe": [],

    "damage": 0,

    "energy": 0,

    "description": " CAUTION! ZOMBIES WAKE UP AT MIDNIGHT... "
}

item_atticNote = {
    "id": "diary",

    "name": "old diary",

    "recipe": [],

    "damage": 1,

    "energy": 0,

    "description": """ how to: construct a parachute, items required: a large sheet, rope, tape and thread  """
}

item_atticNote2 = {
    "id": "paper",

    "name": "crumpled up paer",

    "recipe": [],

    "damage": 0,

    "energy": 0,

    "description": "this note seems very old nothing can be made out "

}

item_wardNote = {
    "id": "drawing",

    "name": "Child's drawing",

    "recipe": [],

    "energy": 0,

    "damage": 0,

    "description": " a drawing of zombies "
}

item_WaitingNote = {
    "id": "tissue",

    "name": "used tissue",

    "recipe": [],

    "damage": 0,
    
    "energy": 0,

    "description": "whoops! this is isn't a note just a crumpled up tissue"
}

item_drink = {
    "id": "drink",

    "name": "Energy drink",

    "recipe": [],

    "damage": 1,

    "energy": 20,

    "description": "The fuel of programmers"
}

item_chocolate = {
    "id": "chocolate",

    "name": "chocolate bar",

    "recipe": [],

    "damage": 1,

    "energy": 10,

    "description": "A packaged chocolate bar, your favourite kind too"
}

item_apple = {
    "id": "apple",

    "name": "apple",

    "recipe": [],

    "damage": 1,

    "energy": 5,

    "description": "Doesn't look the freshest but should do.. "
}

item_card= {
    "id": "card",

    "name": "get well soon card",

    "recipe": [],

    "damage": 0,

    "energy": 0,

    "description": "A get well soon card left to you by your family."
}


item_parachute = {
    "id": "parachute",

    "name": "parachute",

    "recipe": [item_rope, item_suture, item_patients_gown, item_bedsheet],
    
    "damage": 2,
    
    "energy": 0,

    "description": "A parachute made from bedsheets, will this work? who knows!"
}

item_map = {

    "id": "map",

    "name": "map of the hospital",

    "recipe": [],

    "energy": 0,

    "description": """

h::::::::::::::::::::::::::::::::::::::::::::::::::::::::::y
s                       -........-                         o
s                       : ATTIC  :                         o
s                       /........:                         o
s                          :  :                            o
s                          :  :                            o
s                      ....-..-...-         ............-  o
s                      : CHILDREN'S:         :   XRAY    : o
s                      :   WARD   :........./    ROOM    : o
s                      `...:..:....         `............  o
s                          :  :                            o
s                          :  :                            o
s                          :  :                            o
s                        `--..-..:........./```````````.-  o
s                        .P. ROOM:         : OPERATING  :  o
s                        `:-....-:........./  THEATRE  .-  o
s                          :  `-            ```````````    o
s                          :  `-                           o
s                          :  `-                           o
s  .............        -..-...-... -                      o
s  :  WAITING  /......../ RECEPTION :                      o
s  :   ROOM    /......../           :                      o
s  -...........-        -..-...-... :                      o
s                          -`  :                           o
s                          :`  :                           o
s                       `..:...:...`                       o
s                       :   MORGUE :                       o
s                       :          :                       o
s                       `..........`                       o
y::::::::::::::::::::::::::::::::::::::::::::::::::::::::::y
"""
    
}

item_keycard = {
    
    "id": "keycard",

    "name": "keycard",

    "recipe": [],
    
    "damage": 1,
    
    "energy": 0,

    "description": "A keycard, what door is it used for?"

}

item_ladder = {
        
    "id": "ladder",

    "name": "ladder",

    "recipe": [],
    
    "damage": 4,
    
    "energy": 0,

    "description": "A ladder, for elevation"

}

item_key = {
        
    "id": "keys",

    "name": "master key",

    "recipe": [],
    
    "damage": 1,
    
    "energy": 0,

    "description": "A collection of keys on a ring, one of them must be useful right?"

}

item_scalpel = {
        
    "id": "scalpel",

    "name": "surgical scalpel",

    "recipe": [],
    
    "damage": 5,
    
    "energy": 0,

    "description": "A surgical scalpel, looks like it's been used before."

}

item_head = {
        
    "id": "head",

    "name": "human head",

    "recipe": [],
    
    "damage": 1,
    
    "energy": 0,

    "description": "It's a severed human head, rotting around the wound, this is disgusting."

}



items_list = [item_head, item_pen, item_newspaper, item_patients_gown, item_card, item_bedsheet, item_suture, item_rope, item_gun, item_bullets ,item_xrayNote, item_atticNote, item_atticNote2, item_wardNote, item_WaitingNote, item_drink, item_chocolate, item_apple, item_loadedgun,item_parachute, item_map, item_ladder, item_keycard, item_keycard, item_scalpel]
