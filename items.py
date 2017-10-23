item_newspaper = {
    "id": "newspaper",

    "name": "a newspaper",

    "recipe": [],

    "energy": "0",

    "description": 

    """HEADLINE: HYSTERIA IN THE HOSPITAL """

}

item_pen = {
    "id": "pen",
    
    "name": "a pen",

    "recipe": [],

    "energy": "0",

    "description": "A basic ballpoint pen."
}


item_patients_gown = {
    "id": "gown",
    
    "name": "a patients gown",

    "recipe": [],

    "energy": "0",

    "description": "A basic patients gown to keep you warm"
}

item_card = {
    "id": "card",
    
    "name": "a get well soon card",

    "recipe": [],

    "energy": "0",

    "description": "A get well soon card written to you by your family"
}

item_bedsheet = {
    "id": "bedsheet",

    "name": "surgical bedsheets",

    "recipe": [],

    "energy": "0",

    "description": "a pile of bloody bedsheets"
}

item_suture = {
    "id": "suture",

    "name": "surgical suture kit",

    "recipe": [],

    "energy": "0",

    "description": "the kit contains: surgical needles, nylon sutures (thread), scalpel, small scissors, tape"
}

item_rope = {
    "id": "rope",

    "name": "a pile of rope",

    "recipe": [],

    "energy": "0",

    "description": "a thick, dusty rope probably left over from the renovation of the hospital"
}

item_gun = {
    "id":"gun",

    "name": "a classic pistol",

    "recipe": [],

    "energy": "0",

    "description": "oh no! there are no bullets in the pistol, maybe there are lying around somewhere else..."
}





item_bullets = {
    "id": "bullets",

    "name": "a bunch of bullets",

    "recipe": [],

    "energy": "0",

    "description": "a bunch of bullets scattered on the floor, there must be a gun around somewhere..."
}

item_loadedgun = {
    
    "id":"gun_loaded",

    "name": "a classic pistol, loaded",

    "recipe": [item_gun, item_bullets],

    "energy": "0",

    "description": "Shiny and deadly"
}

item_xrayNote = {
    "id": "xray_note",

    "name": "xray note",

    "recipe": [],

    "energy": "0",

    "description": " CAUTION! ZOMBIES WAKE UP AT MIDNIGHT... "
}

item_atticNote = {
    "id": "attic_note",

    "name": "Attic note",

    "recipe": [],

    "energy": "0",

    "description": """ how to: construct a parachute, items required: a large sheet, rope, tape and thread  """
}

item_atticNote2 = {
    "id": "attic_note2",

    "name": "Attic note_2",

    "recipe": [],

    "energy": "0",

    "description": "this note seems very old nothing can be made out "

}

item_wardNote = {
    "id": "Ward_note",

    "name": "Children ward note",

    "recipe": [],

    "energy": "0",

    "description": " a drawing of zombies "
}

item_WaitingNote = {
    "id": "Waiting_note",

    "name": "Waiting room note",

    "recipe": [],

    "energy": "0",

    "description": "whoops! this is isn't a note just a crumpled up tissue"
}

item_drink = {
    "id": "Drink",

    "name": "Energy drink",

    "recipe": [],

    "energy": "35cb",

    "description": "Yay! you have found an energy drink"
}

item_chocolate = {
    "id": "chocolate",

    "name": "chocolate bar",

    "recipe": [],

    "energy": "20",

    "description": "yay! you have found a chocolate bar"
}

item_fruit = {
    "id": "Fruit",

    "name": "An apple",

    "recipe": [],

    "energy": "5",

    "description": "Doesn't look the freshest but should do.. "
}

item_parachute = {
    "id": "parachute",

    "name": "a parachute",

    "recipe": [item_rope, item_suture, item_patients_gown, item_bedsheet],

    "energy": "0",

    "description": "A parachute made from bedsheets, will this work? who knows!"
}






items_list = [item_pen, item_newspaper, item_patients_gown, item_card, item_bedsheet, item_suture, item_rope, item_gun, item_bullets ,item_xrayNote, item_atticNote, item_atticNote2, item_wardNote, item_WaitingNote, item_drink, item_chocolate, item_fruit, item_loadedgun,item_parachute]