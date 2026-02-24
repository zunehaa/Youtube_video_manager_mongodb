import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://code:password@youtube-app-manger.bytqn9n.mongodb.net/", tlsAllowInvalidCertificates= True)

print(client)



db = client["ytmanager"]
video_collection = db["Videos"]



print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
        #print(f'ID: {video['_id']}, Name: {video["name"]}, Time: {video["time"]}')

def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_videos(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': video_id},
        {"$set": {"name": new_name, "time":new_time}}
        )


def delete_videos(video_id):
    video_collection.delete_one({"_id":video_id})




def main():
    while True:
        print("\n\n Youtube App Manager")
        print("1. List Videos")
        print("2. Add video")
        print("3. Update details of video")
        print("4. Delete video")
        print("5. Exit the app")
        choice=input("Enter your choice: ")
        print("\n\n")

        if choice=='1':
            list_videos()

        elif choice=='2':
            name=input("Enter video name: ")
            time=input("Enter video time: ")
            add_videos(name, time)
        
        elif choice=='3':
            video_id = ObjectId(input("Enter video id: "))
            new_name=input("Enter updated video name: ")
            new_time=input("Enter updated video time : ")
            update_videos(video_id, new_name, new_time)

        elif choice=='4':
            video_id = ObjectId(input("Enter video id: "))
            delete_videos(video_id)

        elif choice=="5":
            break
        else:
            print("Invalid choice!")


if __name__=="__main__":
    main()