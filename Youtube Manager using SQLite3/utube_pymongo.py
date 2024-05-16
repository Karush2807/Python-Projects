import pymongo

client= pymongo.MongoClient("mongodb+srv://nigga2807:244466666@youtubemanager.8ssqukg.mongodb.net/")
#not a good practice to hardcode the password

db=client['youtubemanager']
video_collection=db['videos']

print(video_collection.find_one())