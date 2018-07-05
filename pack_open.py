#!/Users/mohit/anaconda/bin/python
# TODO: remove shebang line for export
# TODO: remove shebang line for export
import sys
from random import shuffle
import random

class Card:
	# TODO: add cost, attack, and health variables
	def __init__(self, _name):
		self.n = _name

	# "Life of the party", "Plant food", etc.
	def reset_name(self, _name):
		self.n = _name
	def get_name(self):
		return self.n

	# "zombie" or "plant"
	def set_faction(self, _faction):
		self.f = _faction
	def get_faction(self):
		return self.f

	# "beastly", "smarty", etc.
	def set_class(self, _class):
		self.c= _class
	def get_class(self):
		return self.c

	# "imp", "leafy", etc. (given as a list)
	# Tricks/Environents are considered to be tribes (i.e. the "environment pack")
	def set_tribes(self, _tribes):
		self.t = _tribes
	def get_tribes(self):
		return self.t

	# "basic", "premium", "galactic", "colossal", "triassic".
	# Event cards are considered set-less
	def set_set(self, _set=None):
		self.s = _set
	def get_set(self):
		return self.s

	# "uncommon", "rare", "superrare", "event", or "legendary"
	def set_rarity(self, _rarity):
		self.r = _rarity
		self.set_spark_value()
	def get_rarity(self):
		return self.r

	# "Team-up", "Bullseye", etc. (given as a list)
	def set_attributes(self, _attributes=[]):
		self.a = _attributes
	def get_attributes(self):
		return self.a

	# "When destroyed: Do 2 damage to Zombie here", etc.
	def set_effect(self, _effect=None):
		self.e = _effect
	def get_effect(self):
		return self.e

	# "He always knows what time it is. CRAZY TIME!", etc.
	def set_description(self, _description):
		self.d = _description
	def get_description(self):
		return self.d

	def set_spark_value(self):
		if self.r == "Uncommon":
			self.v = 15
		elif self.r == "Rare":
			self.v = 50
		elif self.r == "Super-Rare" or "Event":
			self.v = 250
		elif self.r == "Legendary":
			self.v = 1000
		else:
			# debugging: shouldn't be an external way to call this
			print("No rarity set for this card. Set a rarity first.")
	def get_spark_value(self):
		return self.v

	def set_keywords(self):
		self.k = []
		self.k.append(self.get_name())
		self.k.append(self.get_faction())
		self.k.append(self.get_class())
		self.k.extend(self.get_tribes())
		self.k.append(self.get_set())
		self.k.append(self.get_rarity())
		self.k.extend(self.get_attributes())
		self.k.append(self.get_spark_value())
	def get_keywords(self):
		return self.k

class Pack:
	# TODO: initialization needs to include set name or tribe type
	def __init__(self):
		self.contents = []
		self.total = {'uncommon':0, 'rare':0, 'superrare':0, 'event':0, 'legendary':0}
		self.pack_prob = 1
		# This will serve as assertion to make sure a pack has been filled
		self.is_filled = False

	# Manually fill the cards in a pack. No return.
	def manually_fill(self, cards):
		# Manually filled packs can have any number of cards or rarity spread
		for card in cards:
			self.total[card.get_rarity()] += 1
			self.contents.append(card)
		self.is_filled = True

	# Fill pack according to standard rarity breakdown. No return.
	def auto_fill(self, _cards):
		# Each pack will have at least 3 uncommons, 1 rare,
		# 1 super-rare (or another uncommon), and 1 legendary (or another uncommon)
		self.total['uncommon'] = 3
		self.total['rare'] = 1

		# Check if you'll get a super-rare
		if random.random() <= 0.3:
			self.total['superrare'] += 1
			self.pack_prob *= 0.3
		else:
			self.total['uncommon'] += 1
			self.pack_prob *= 0.7

		# Check if you'll get a legendary
		if random.random() <= 0.1:
			self.total['legendary'] += 1
			self.pack_prob *= 0.1
		else:
			self.total['uncommon'] += 1
			self.pack_prob *= 0.9

		# TODO: add logic to choose correct set instead of all cards
		# TODO change logic to handle collection as dictionary insteado of list
		# Reminder: need this clunky logic because of replacement
		# Randomly select 3-5 uncommons from all cards 
		_total_uncommons = 0
		while _total_uncommons < self.total['uncommon']:
			shuffle(_cards)
			for _card in _cards:
				if _card.get_rarity() == "uncommon":
					self.contents.append(_card)
					_total_uncommons += 1
					break

		# Randomly select 1 rare from all cards 
		_total_rares = 0
		while _total_rares < self.total['rare']:
			shuffle(_cards)
			for _card in _cards:
				if _card.get_rarity() == "rare":
					self.contents.append(_card)
					_total_rares += 1
					break

		# Randomly select 0-1 super-rares from all cards 
		_total_superrares = 0
		while _total_superrares < self.total['superrare']:
			shuffle(_cards)
			for _card in _cards:
				if _card.get_rarity() == "superrare":
					self.contents.append(_card)
					_total_superrares += 1
					break

		# Randomly select 0-1 legendaries from all cards 
		_total_legendaries = 0
		while _total_legendaries < self.total['legendary']:
			shuffle(_cards)
			for _card in _cards:
				if _card.get_rarity() == "legendary":
					self.contents.append(_card)
					_total_legendaries += 1
					break

		self.is_filled = True

	# Return cards in pack as a simple list
	def get_cards(self):
		cards = []
		for card in self.contents:
			cards.append(card)
		return cards

	# Prints cards in a pack as a simple list. No return.
	def view_cards(self):
		# TODO: group and sort contents so uncommons -> rares -> super-rares -> legendaries display	
		card_names = []
		for card in self.contents:
			card_names.append(card.get_name())
		print (card_names)



	# Display how the rarities broke down. Set view_mode=True for a more readable option. No return.
	def view_summary(self, view_mode=False):
		
		if view_mode == True:
			print ("Uncommons:%d | Rares:%d | Super-Rares:%d | Legendaries:%d" % (self.total['uncommon'], self.total['rare'], self.total['superrare'], self.total['legendary']), "| Probability of pack=%d%%" % (self.pack_prob*100.))
		else:
			print ([self.total['uncommon'], self.total['rare'], self.total['superrare'], self.total['legendary'], self.pack_prob])

class MultiPack:
	def __init__(self):
		self.contents = []
		self.total = {'uncommon':0, 'rare':0, 'superrare':0, 'event':0, 'legendary':0}
		# TODO: allow user to specify which size multipack
		self.num_packs = 11
		self.is_filled = False

	def view_packs(self):
		for pack in self.contents:
			pack.view_cards()

	def view_packs_summary(self, view_mode=False):
		for pack in self.contents:
			pack.view_summary(view_mode)

	# Fill multipack by independently filling single packs and dumping in their contents
	def fill(self, collection):
		for pack in range(self.num_packs):
			new_pack = Pack()
			new_pack.auto_fill(collection)
			# # version2: merge dictionaries while filling. Not working b/c it loses keys that are 0 ('legendary', usually)
			# merge_two_dictionaries() function has been removed
			# self.total = merge_two_dicts(new_pack.total, self.total)
			# print self.total
			self.contents.append(new_pack)

		# version1: Just go through all cards again and add up rarities
		for card in self.get_cards():
			self.total[card.get_rarity()] += 1
		

		self.is_filled = True
			

	# Will return all cards in multipack as list of cards
	def get_cards(self):
		cards = []
		for pack in self.contents:
			cards.extend(pack.get_cards())
		return cards

	# Prints cards in a pack as a simple list. No return.
	def view_cards(self):
		card_names = []
		for card in self.get_cards():
			card_names.append(card.get_name())
		print (card_names)

	# Combined view showing summary of whole mulitpack
	def view_summary(self, view_mode=False):
		if view_mode == True:
			print ("Uncommons:%d | Rares:%d | Super-Rares:%d | Legendaries:%d" % (self.total['uncommon'], self.total['rare'], self.total['superrare'], self.total['legendary'])) #, "| Probability of pack=%d%%" % (self.pack_prob*100.)
		else:
			print ([self.total['uncommon'], self.total['rare'], self.total['superrare'], self.total['legendary']]) # self.pack_prob found with binomial dist


def create_collection_v2():
	# TODO change this to return a dictionary
	#  = Card("")
	# .set_faction("")
	# .set_class("")
	# .set_tribes([])
	# .set_set("")
	# .set_rarity("")
	# .set_attributes([])
	# .set_effect()
	# .set_description("")

	potato_mine = Card("Potato Mine")
	potato_mine.set_faction("plant")
	potato_mine.set_class("guardian")
	potato_mine.set_tribes(["root"])
	potato_mine.set_set("premium")
	potato_mine.set_rarity("uncommon")
	potato_mine.set_attributes(["team-up"])
	potato_mine.set_effect("When destroyed: Do 2 damage to a Zombie there")
	potato_mine.set_description("I'm starchy and explosive!")

	cactus = Card("Cactus")
	cactus.set_faction("plant")
	cactus.set_class("guardian")
	cactus.set_tribes(["cactus", "flower"])
	cactus.set_set("premium")
	cactus.set_rarity("uncommon")
	cactus.set_attributes(["bullseye"])
	cactus.set_effect()
	cactus.set_description("It's true. I'm prickly on the outside but spongy on the inside.")

	pool_shark = Card("Pool Shark")
	pool_shark.set_faction("zombie")
	pool_shark.set_class("brainy")
	pool_shark.set_tribes(["mustache", "sports"])
	pool_shark.set_set("premium")
	pool_shark.set_rarity("uncommon")
	pool_shark.set_attributes(["bullseye"])
	pool_shark.set_effect()
	pool_shark.set_description("Not actually a shark")

	space_ninja = Card("Space Ninja")
	space_ninja.set_faction("zombie")
	space_ninja.set_class("crazy")
	space_ninja.set_tribes(["professional"])
	space_ninja.set_set("galactic")
	space_ninja.set_rarity("uncommon")
	space_ninja.set_attributes([])
	space_ninja.set_effect("While in an Environment: The first time each turn this does damage, do 1 damage to each Plant")
	space_ninja.set_description("You will never hear him coming in the vacuum of space.")

	zombie_coach = Card("Zombie Coach")
	zombie_coach.set_faction("zombie")
	zombie_coach.set_class("hearty")
	zombie_coach.set_tribes(["mustache", "sports"])
	zombie_coach.set_set("premium")
	zombie_coach.set_rarity("rare")
	zombie_coach.set_attributes([])
	zombie_coach.set_effect("When played: All Sports Zombies can't be hurt this turn")
	zombie_coach.set_description("There's no 'i' in Zombee!")

	lazer_base_a = Card("Laser Base Alpha")
	lazer_base_a.set_faction("zombie")
	lazer_base_a.set_class("sneaky")
	lazer_base_a.set_tribes(["science", "environment"])
	lazer_base_a.set_set("galactic")
	lazer_base_a.set_rarity("superrare")
	lazer_base_a.set_attributes([])
	lazer_base_a.set_effect("Zombies here get Deadly and Strikethrough")
	lazer_base_a.set_description("Zombies with LASERS. What could possibly go wrong?")

	nut_bowling = Card("Wall Nut Bowling")
	nut_bowling.set_faction("plant")
	nut_bowling.set_class("guardian")
	nut_bowling.set_tribes(["nut", "trick"])
	nut_bowling.set_set("premium")
	nut_bowling.set_rarity("legendary")
	nut_bowling.set_attributes([])
	nut_bowling.set_effect("Make a Wall-Nut in each Ground lane. Attack for 6 damage in those lanes.")
	nut_bowling.set_description("Ugly shoes not required!")

	# return_dict = {'uncommon':[], 'rare':[], ''}
	temp_list = [potato_mine, cactus, pool_shark, space_ninja, zombie_coach, lazer_base_a, nut_bowling]
	# for card in temp_list:


def create_collection():
	# TODO change this to return a dictionary
	#  = Card("")
	# .set_faction("")
	# .set_class("")
	# .set_tribes([])
	# .set_set("")
	# .set_rarity("")
	# .set_attributes([])
	# .set_effect()
	# .set_description("")

	potato_mine = Card("Potato Mine")
	potato_mine.set_faction("plant")
	potato_mine.set_class("guardian")
	potato_mine.set_tribes(["root"])
	potato_mine.set_set("premium")
	potato_mine.set_rarity("uncommon")
	potato_mine.set_attributes(["team-up"])
	potato_mine.set_effect("When destroyed: Do 2 damage to a Zombie there")
	potato_mine.set_description("I'm starchy and explosive!")

	cactus = Card("Cactus")
	cactus.set_faction("plant")
	cactus.set_class("guardian")
	cactus.set_tribes(["cactus", "flower"])
	cactus.set_set("premium")
	cactus.set_rarity("uncommon")
	cactus.set_attributes(["bullseye"])
	cactus.set_effect()
	cactus.set_description("It's true. I'm prickly on the outside but spongy on the inside.")

	pool_shark = Card("Pool Shark")
	pool_shark.set_faction("zombie")
	pool_shark.set_class("brainy")
	pool_shark.set_tribes(["mustache", "sports"])
	pool_shark.set_set("premium")
	pool_shark.set_rarity("uncommon")
	pool_shark.set_attributes(["bullseye"])
	pool_shark.set_effect()
	pool_shark.set_description("Not actually a shark")

	space_ninja = Card("Space Ninja")
	space_ninja.set_faction("zombie")
	space_ninja.set_class("crazy")
	space_ninja.set_tribes(["professional"])
	space_ninja.set_set("galactic")
	space_ninja.set_rarity("uncommon")
	space_ninja.set_attributes([])
	space_ninja.set_effect("While in an Environment: The first time each turn this does damage, do 1 damage to each Plant")
	space_ninja.set_description("You will never hear him coming in the vacuum of space.")

	zombie_coach = Card("Zombie Coach")
	zombie_coach.set_faction("zombie")
	zombie_coach.set_class("hearty")
	zombie_coach.set_tribes(["mustache", "sports"])
	zombie_coach.set_set("premium")
	zombie_coach.set_rarity("rare")
	zombie_coach.set_attributes([])
	zombie_coach.set_effect("When played: All Sports Zombies can't be hurt this turn")
	zombie_coach.set_description("There's no 'i' in Zombee!")

	lazer_base_a = Card("Laser Base Alpha")
	lazer_base_a.set_faction("zombie")
	lazer_base_a.set_class("sneaky")
	lazer_base_a.set_tribes(["science", "environment"])
	lazer_base_a.set_set("galactic")
	lazer_base_a.set_rarity("superrare")
	lazer_base_a.set_attributes([])
	lazer_base_a.set_effect("Zombies here get Deadly and Strikethrough")
	lazer_base_a.set_description("Zombies with LASERS. What could possibly go wrong?")

	nut_bowling = Card("Wall Nut Bowling")
	nut_bowling.set_faction("plant")
	nut_bowling.set_class("guardian")
	nut_bowling.set_tribes(["nut", "trick"])
	nut_bowling.set_set("premium")
	nut_bowling.set_rarity("legendary")
	nut_bowling.set_attributes([])
	nut_bowling.set_effect("Make a Wall-Nut in each Ground lane. Attack for 6 damage in those lanes.")
	nut_bowling.set_description("Ugly shoes not required!")

	return [potato_mine, cactus, pool_shark, space_ninja, zombie_coach, lazer_base_a, nut_bowling]

def set_collection_keywords(collection):
	for card in collection:
		card.set_keywords()

# takes the full collection, keyword, and keyword type as argument and returns filtered list matching the keyword
def filter_collection(collection, keyword, type=None):
	# make empty list
	# iterate through collection
	# if keyword found on card, append it to empty list (if type given, check keyword is that type for card)
	# return list

	filtered_collection = []
	for card in collection:
		if keyword in card.get_keywords():
			filtered_collection.append(card)

	return filtered_collection



def show_pack(collection):
	# Create a new pack, fill it with cards
	new_pack = Pack()
	new_pack.auto_fill(collection)
	
	# Debugging: print contents and a human readable summary
	new_pack.view_cards()
	new_pack.view_summary(True)

def show_multipack(collection):
	new_multi = MultiPack()
	new_multi.fill(collection)
	
	# Debugging: print contents and a human readable summary
	# new_multi.view_packs()
	new_multi.view_packs_summary(True)
	# new_multi.view_cards()
	new_multi.view_summary(True)


## ------ MAIN STARTS HERE ------- ##


collection = create_collection()
# temporary, so it isn't loading in keywords each time
set_collection_keywords(collection)
filtered_collection = filter_collection(collection, "guardian")


#show_pack(collection)
#show_multipack(collection)


sys.exit()