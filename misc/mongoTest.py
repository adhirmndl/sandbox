from pymongo import MongoClient

client = MongoClient('10.16.65.182:27017')

db = client['test']

collection = db['testData']
print collection.insert({	'author' : 'ABCD',
							'text' : 'acdadf'
						})


print db.collection_names()

print db.find_one()