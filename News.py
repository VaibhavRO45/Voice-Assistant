import requests
from ss import *

Key = "2ac3a69ade024dea9582fbb21c34ab61"

api_address = "https://newsapi.org/v2/everything?q=keyword&apiKey=" +Key
json_data = requests.get(api_address).json()

ar =[]
def news():
    for i in range(3):
        ar.append("Number "+str(i+1) + " , " + json_data["articles"][i]["title"]+ ".")

    return ar
#arr = news()
#print(arr)