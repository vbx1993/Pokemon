import Pokemon

class Trainer:
	def __init__(self, name, pokemon, items=None):
		self.name = name
		if len(pokemon) > 6:
			print("You cannot register more than 6 pokemon to battle")
			raise RuntimeError
		if len(pokemon) < 1:
			print("You must register at least 1 pokemon to battle")
			raise RuntimeError
		self.pokemon = [Pokemon(poke_name) for poke_name in pokemon]
		# Now let's load the trainer backpack with items!
		starter_items = ['super potion', "antidote", "berry"]
		self.backpack = [Item(item_name) for item_name in starter_items]
		if items:
			for item_name in items:
				self.backpack.append(Item(item_name))