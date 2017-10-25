from items import *

room_OT={
	"name": "Operating Theatre",

	"description": 
	 """    You go into the Operating Theatre in front of you is a half operated on body. 
	 It's chest wide open with a scalpel inserted between the fourth and fifth rib.  
	 There are dozens of surgical drape sheets scattered around the room as if a savage animal had been set aloose... 
	 You walk up to the body and are fixated upon the fresh bullet hole between the victims eyes.
	 You look about more and there are plenty of surgial cuboards for you to look through.
	 """,

	 "exits": {"left":"Patient_Room"},

	 "items": [item_bedsheet, item_suture],

	 "containers": {"tray": [],"cupboard": [],"corpse": [], "table":[], "floor":[item_bullets] }

}

room_Waiting={
	"name": "Waiting Room",

	"description":
	"""    You walk in and there is an eerie silence in the derelict room, nothing to search through only rows of empty seats...""",

	"exits": {"right":"Reception"},

	"items": [item_apple, item_WaitingNote, item_gun],

	"containers": {"cupboard": [], "seats": [], "floor": [item_ladder] }
	
}

room_Xray={
	"name": "Xray Room",

	"description":
	"""    Immediately after entering the room you are greeted by the humming of grand x-ray machines and a dingey ultra green light...
	The machines are battered and on however there is no obvious way of turning it off especially as the contorl panal is damaged.
	With each step around the room the faint sound of crunching paper arises above the humming of machines. 
	You then realise there are research notes all over the floor.
	Could there be any useful information amongst the scattered notes?

	  """,

	"exits": {"left":"Children_Ward"},

	"items": [],

	"containers": {"cupboard": [],"desk": [], "body":[], "floor": [item_xrayNote] }

}

room_reception={
	"name": "Reception",

	"description":
	"""    As you walk into reception you see bolted doors sealed with rusty bars plastered with "DO NOT ENTER" signs from the outside. 
    You can see bloody handprints against the locked doors, pools of blood swimming with empty shells infront of them. 
    There is a newspaper sat on the receptionist desk the only thing left not broken, kicked in or dripping in blood. 
    The newspaper could explain what has happened to the town.
    You hear footsteps from upstairs and splitting screams from distances outside.
    There is a door leading downstairs, but it requires a keycard to pass through.""",

	"exits": {"left":"Waiting_Room", "down":"Morgue"},

	"items": [item_newspaper, item_apple],

	"containers": {"cupboard": [],"desk": []}


}

room_attic={

	"name": "Attic",

	"description": 
	"""    Reaching the top of the ladder, you promptly survey the room, or at least as much as you can as it is near total darkness.
	You can see decrepit furniture, what seems like ancient cots and an old machine covered in a thick layer of dust.
	You don't know what purpose the machine had served but it looks like some kind of surgical instrument.
	There is also old boxes of files, likely redundant due to the medical databases.""",

	"exits": {"down":"Children_Ward"},

	"items": [item_atticNote2, item_atticNote, item_rope, item_keycard],

	"containers": {"cupboard": [],"machine": [],"boxes": []},

	"ladder": False

}

room_morgue={
	"name": "Morgue",

	"description":
	"""    The lights in the corrider are flickering. As you walk into the morgue, you stumble upon coffins scattered around. Walls splattered with blood.
        You've decided to examine each coffins. As you examine further, you start to realize movement from the bodies placed in the coffin.
        Towards the last coffin, you come across a sign which says "Be Aware of Zombies".""",

	"exits": {"upstairs":"Reception"},

	"items": [item_rope],

	"containers": {"cupboard": [],"drawers": [], "refrigerator":[]},

}

room_ChildrenWard={
	"name": "The Children's Ward",

	"description":
	"""     Right after you step foot into the Children's Ward, you are welcomed by whispering of children's voices.
		 The room looked like it was never damaged
         whcih brings a uneartly feeling. You come across a note left in the room.
         Would the note benefit you in any way possible? 
         You notice there is an opening above you but you would need to attach a ladder to get up there.""",

	"exits": {"up":"Attic", "right":"Xray", "downstairs":"Patient_Room"},

	"items": [item_drink, item_wardNote],

	"containers": {"bed": [],"toybox": [],"drawers": []}

}

room_PatientRoom={
	"name": "The Patient's Room",

	"description":
	""" In one of the scariest night you woke up on a bed. You hear water droplets dripping on the window panes. 
	First thing you realized is you are left alone in the darkness and you are unaware of your whereabouts. 
	You then noticed you are wrapped around in a hospital gown. """,

	"exits": {"right":"OT", "downstairs":"Reception", "upstairs":"Children_Ward"},

	"items": [item_chocolate],

	"containers": {"drawers": [item_map], "bed":[], "gift":[item_card]},
}

rooms ={
"OT": room_OT,
"Waiting_Room": room_Waiting,
"Xray": room_Xray,
"Reception": room_reception,
"Attic": room_attic,
"Morgue": room_morgue,
"Children_Ward": room_ChildrenWard,
"Patient_Room": room_PatientRoom
	
}
