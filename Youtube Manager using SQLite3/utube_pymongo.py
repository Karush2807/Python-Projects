import pymongo
from bson import ObjectId

client= pymongo.MongoClient("mongodb+srv://nigga2807:244466666@youtubemanager.8ssqukg.mongodb.net/")
#not a good practice to hardcode the password

print(client)
db=client['youtubemanager'] #database created
video_collection=db['videos']

print(video_collection)

def add_videos(name, time):
    video_collection.insert_one({'name':name,'time':time})

def list_videos():
    for video in video_collection.find():
        print(
            f"ID: {video['_id']}, "
            f"Video name: {video['Video Name']}, "  # Assuming 'Name' is the correct field name
            f"Time: {video['Video Time']}"  # Assuming 'Time' is the correct field name
        )

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
    {'_id': ObjectId(video_id)},
    {"$set": {"name": new_name, "time": new_time}}
    )
    
    

def delete_video(vid_id):
    video_collection.delete_one(
        {'_id':ObjectId(vid_id)})


def exit():
    pass

def main():
    while True:
        print("\n UTube Manager!!")
        print("1. List ALL Videos")
        print("2. ADD Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice =='1':
            list_videos()

        elif choice =='2':
            name=input("Enter the name of the video: ")
            time=input("Enter the time of the video: ")
            add_videos(name, time)
        
        elif choice =='3':
            vid_id=input("Enter the  video id: ")
            nname=input("Enter the  updated name of the video: ")
            ntime=input("Enter the  updated time of the video: ")

            update_video(vid_id, nname, ntime)

        elif choice == '4':
            vid_id=input("Enter the video id to be deleted: ")
            delete_video(vid_id)
        
        else:
            break

if __name__ == '__main__':
    main()