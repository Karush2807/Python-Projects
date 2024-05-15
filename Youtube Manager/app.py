import json

def load_data(): #data load ek file se hoga!!
    try:
        with open("utube.txt", 'r') as file:
            return json.load(file)
            #this statement json.load(file), reads data from a specofc file and parses into python object, dictonary or list
            #it doesnt print anything it return the parsed python object containing json data
    except FileNotFoundError:
        print("File not found!!")
        return []

def save_data_helper(videos):
    with open("utube.txt", 'w') as file:
        json.dump(videos, file)
    

# this will show all the videao makred fav by the user
def all_videos(videos):
    # for index, vid in enumerate(videos, start=1):
    #     return print(f"{index}-->. {vid['video name']} {vid['video duration']} {vid['Vid URL']}")
    # print(videos)
    print('\n')
    print('*'*80)
    for index, vid in enumerate(videos, start=1):
        
        print(f"{index}. {vid['video name']} {vid['video duration']} {vid['Vid URL']}")
    print('*'*80)
#this will tell the duration of the youtube video
def durn_of_vid(videos):
    pass

#this will update the video details
def updt_vid(videos):
    all_videos(videos)
    input_index=int(input("enter which index u want to update: "))
    if 1<=input_index<=len(videos):
        n_name=input("enter the new name: ")
        n_duration=input("enter the new duration:")
        n_link=input("enter the new link:")

        videos[input_index-1]={'name':n_name, 'duration':n_duration,
        'link':n_link}
        save_data_helper(videos)

    else:
        print("Invalid index selected!!")



#this will add a video to the list
def add_vid(videos):
    vid_name=input("enter the video name: ")
    vid_duration=input("enter the video duration: ")
    vid_link=input("enter the video link: ")
    videos.append({'video name': vid_name, 'video duration':vid_duration, 'Vid URL': vid_link})
    save_data_helper(videos)

#this will search the video
def search_vid(videos):
    find_index=int(input("enter the index u need to search: "))
    if 1<=find_index<=len(videos):
        print(f"Video name: {videos[find_index-1]['video name']}")
        print(f"Video Duration: {videos[find_index-1]['video duration']}")

#this will delete the video
def del_vid(videos):
    del_index=int(input("enter the index u want to delete:"))
    if 1<=del_index<=len(videos):
        del videos[del_index-1] #synatx for deleting an element from a list
        save_data_helper(videos)
    else:
        print("invalid index selected!!")

#this will exit the program
def exit():
    pass



def main():
    videos=load_data()
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
        # print("videos")

        match choice:
            case "1":
                all_videos(videos)
            
            case "2":
                durn_of_vid(videos)
            
            case "3":
                updt_vid(videos)
            
            case "4":
                add_vid(videos)
            
            case "5":
                search_vid(videos)
            
            case "6":
                del_vid(videos)
            
            case "7":
                exit(videos)
            
            case _:
                print("Invalid choice!!")

if __name__== "__main__":
    main()
