from django.shortcuts import render, HttpResponse, redirect
from .keys import *
from pprint import pprint
from pymongo import MongoClient

# Create your views here.
def home(request):
    return render(request, "home.html")

def segregate(request):
    return render(request, "segregate.html")

def bin(request):
    # run only if a post request is made
    # using the mongoDB
    if request.method == "POST":
        items = request.POST.get('waste')
        cluster = MongoClient(link)
        db = cluster["waste"]
        collection = db["waste"]

        itemList = items.split(", ")
        print(itemList)

        # creating empty lists for each category of waste
        notFound = []
        hazard = []
        biomed = []
        elec = []
        house = []
        recyc = []
        green = []

        # if item found in the database, then append it to the lists
        for item in range(len(itemList)):
            data = collection.find_one({'name': itemList[item]})
            if data is None:
                notFound.append(itemList[item])
            else:
                if data['category'] == "hazardous":
                    hazard.append(itemList[item])

                elif data['category'] == "biomedical":
                    biomed.append(itemList[item])

                elif data['category'] == "electronic":
                    elec.append(itemList[item])

                elif data['category'] == "household":
                    house.append(itemList[item])

                elif data['category'] == "recyclable":
                    recyc.append(itemList[item])

                elif data['category'] == "green":
                    green.append(itemList[item])

        # passing context to render the template
        context = {'hazard': hazard, 
        'biomed': biomed, 
        'elec': elec, 
        'house': house, 
        'recyc': recyc, 
        'green': green,
        'notFound': notFound} 
        
        return render(request, template_name="bin.html", context=context)
    
    return render(request, "bin.html")
    

