import requests
#from ss import *

#Key = "2ac3a69ade024dea9582fbb21c34ab61"

#api_address = "https://newsapi.org/v2/everything?q=keyword&apiKey=" +Key

url = "https://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()

arr =["",""]
arr[0] = json_data["setup"]
arr[1] = json_data["punchline"]

def joke():
    return arr


'''def news():
    for i in range(3):
        ar.append("Number "+str(i+1) + " , " + json_data["articles"][i]["title"]+ ".")

    return ar'''
#arr = news()
#print(arr)