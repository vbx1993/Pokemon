class Move:

    def __init__(self, name):
        self.name = name
        load_move_dict(self.name)

    def load_move_dict(name):
    	if name == "rain dance":
    		self.properties = {
    			"type": "water",
    			"PP": 5,
    			"power": None,
    			"weather effect": {
    				"water": 1.5,
    				"fire": 0.5
    			}
    			"accuracy": 100,
    			"status effect": None
    		}
    	if name == "water gun":
    		self.properties = {
    			"type": "water",
    			"PP": 25,
    			"power": 40,
    			"weather effect": None,
    			"accuracy": 100,
    			"status effect": None
    		}
    	if name == "bite":
    		self.properties = {
    			"type": "dark",
    			"PP": 25,
    			"power": 60,
    			"weather effect": None,
    			"accuracy": 100,
    			"status effect": {"flinch": 0.3}
    		}
    	if name == "protect":
    		self.properties = {
    			"type": "normal",
    			"PP": 5,
    			"power": None,
    			"weather effect": None,
    			"accuracy": 100,
    			"status effect": None,
    			"damage effect": 0
    		}
