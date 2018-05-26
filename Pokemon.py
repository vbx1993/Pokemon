import Moves

class Pokemon:

    def __init__(self, name):
        self.name = name
        self.load_traits_dict(self.name)
        self.moves = [Move(move) for move in self.traits["moves"]]


        # self.type = poke_dict[self.name]["type"]
        # self.level = poke_dict[self.name]["level"]
        # self.hp = poke_dict[self.name]["hp"]
        # self.attack = poke_dict[self.name]["attack"]
        # self.defense = poke_dict[self.name]["defense"]
        # self.speed = poke_dict[self.name]["speed"]
        # self.special_attack = poke_dict[self.name]["special_attack"]
        # self.special_defense = poke_dict[self.name]["special_defense"]
        # self.speed = poke_dict[self.name]["speed"]

    def load_traits_dict(self, name):
        if name == "squirtle":
        	self.traits = {
			"type": "water",
			"level": 25,
			"hp": 80,
			"attack": 50,
			"defense": 60,
			"special_attack": 60,
			"special_defense": 70,
			"speed": 80,
			"moves": ["water gun", "rain dance", "bite", "protect"]
		}
		# LOAD ALL POSSIBLE POKEMON HERE???? VIA A GIANT IF SWITCH??
		#if name == 