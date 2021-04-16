from pymongo import MongoClient

def find():
    link = f"mongodb+srv://anish:anish2606@cluster0.2kyic.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    cluster = MongoClient(link)
    db = cluster["waste"]
    collection = db["waste"]

    items = input("Enter your waste to categorize: ")
    itemList = items.split(", ")
    print(itemList)
    notFound = []
    for item in range(len(itemList)):
        data = collection.find_one({'name': itemList[item]})
        if data is None:
            notFound.append(itemList[item])
        else:
            print(itemList[item] + " : " + data['category'])
    
    print(f"Items that were not found in the database: {notFound}")
    
find()





