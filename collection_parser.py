#!/Users/mohit/anaconda/bin/python

import csv
import pack_open as pvzh

# with open('collection.csv', 'rb') as csvfile:
# 	collection_reader = csv.reader(csvfile, delimiter=',')
# 	collection_reader

collection = []

with open('collection.csv', 'rb') as csvfile:
	collection_reader = csv.reader(csvfile, delimiter=',')
	csv_headings = next(collection_reader)
	print "Headers", csv_headings
	for card_id, row in enumerate(collection_reader):
		# print row
		card_id = pvzh.Card(row[0])
		card_id.set_faction(row[1])
		card_id.set_class(row[2])
		card_id.set_tribes(row[3])
		card_id.set_set(row[4])
		card_id.set_rarity(row[5])
		card_id.set_attributes(row[6])
		card_id.set_effect(row[7])
		card_id.set_description(row[8])
		collection.append(card_id)

# for card in collection:
# 	card.set_keywords()
# 	print card.get_name(), card.get_keywords().values()

pvzh.open_pack(collection)