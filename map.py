from items import *

room_OT={
	"name": "Operating Theatre",

	"description": 
	 """    You go into the Operating Theartre in front of you is a half operated on body, chest wide open with a scalpel inserted between the fourth and fifth rib.  
	 There are dozens of surgical drape sheets scattered around the room as if a savage animal had been set aloose... 
	 You walk up to the body and are fixated upon the fresh bullet hole between the victims eyes. 
	 There are also unused bullets by the victims head.
	 You look about more and there are plenty of surgial cuboards for you to look through.
	 """,

	 "exits": {"left":"Patient_Room", "right":"Xray"},

	 "items": [],

	 "containers": []

}

room_Waiting={
	"name": "Waiting Room",

	"description":
	"""    You walk in and there is an eerie silence in the derelict room, nothing to search through only rows of empty seats...""",

	"exits": {"right":"Reception", "left":"Patient_Room"},

	"items": [],

	"containers": []
	
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

	"exits": {"left":"OT"},

	"items": [],

	"containers": []
}

room_reception={
	"name": "Reception",

	"description":
	"""    As you walk into reception you see bolted doors sealed with rusty bars plastered with "DO NOT ENTER" signs from the outside. 
    You can see bloody handprints against the locked doors, pools of blood swimming with empty shells infront of them. 
    There is a newspaper sat on the receptionist desk the only thing left not broken, kicked in or dripping in blood. 
    The newspaper could explain what has happened to the town.
    You hear footsteps from upstairs and splitting screams from distances outside.""",

	"exits": {"left":"Waiting_Room", "right":"Children_Ward"},

	"items": [item_newspaper],

	"containers": []


}

room_attic={
	"name": "Attic",

	"description": 
	"""    Reaching the top of the ladder, you promptly survey the room, or at least as much as you can as it is near total darkness.
	You can see decrepit furniture, what seems like ancient cots and an old machine covered in a thick layer of dust.
	You don't know what purpose the machine had served but it looks like some kind of surgical instrument.
	There is also old boxes of files, likely redundant due to the medical databases.""",

	"exits": {"down":"Children_Ward"},

	"items": [],

	"containers": []
}

room_morgue={
	"name": "Morgue",

	"description":
	""" """,

	"exits": {},

	"items": [],

	"containers": []
}

room_ChildrenWard={
	"name": "The Children's Ward",

	"description":
	""" """,

	"exits": {"up":"Attic", "left":"Reception"},

	"items": [],

	"containers": []

}

room_PatientRoom={
	"name": "The Patient's Room",

	"description":
	""" """,

	"exits": {"right":"Waiting_Room", "left":"OT"},

	"items": [],

	"containers": []
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