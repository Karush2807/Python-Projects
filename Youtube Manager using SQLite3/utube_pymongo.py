import pymongo

client= pymongo.MongoClient("mongodb+srv://karushpy:karushpy@youtubemanager.8ssqukg.mongodb.net/youtubemanager")
#not a good practice to hardcode the password

db=client['youtubemanager']
video_collection=db['videos']

print(video_collection.find_one())