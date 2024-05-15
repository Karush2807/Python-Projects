

# this will show all the videao makred fav by the user
def all_videos(videos):
    pass

#this will tell the duration of the youtube video
def durn_of_vid(videos):
    pass

#this will update the video details
def updt_vid(videos):
    pass

#this will add a video to the list
def add_vid(videos):
    pass

#this will search the video
def search_vid(videos):
    pass

#this will delete the video
def del_vid(videos):
    pass

#this will exit the program
def exit():
    pass

videos=[]

while True:
    print("\n Welcome To The UTube Manager!!")
    print("Choose an option from the following:")
    print("1. List ur pasandida videos")
    print("2. Duration of UTube videos")
    print("3. video ki deatails update")
    print("4. Add a utube video")
    print("5. Search a UTube video")
    print("6. Delete a UTube video")
    print("7. Exit")
    choice=input("Enter your choice: ")

    match choice:
        
        case "1":
            all_videos(videos)