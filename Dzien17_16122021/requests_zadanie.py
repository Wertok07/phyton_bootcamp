import requests
#
# response = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")
#
# print(response.json())
#
# data = response.json()[0]['rates']
#
# for res in data:
#     print(res["code"])



#url = "https://www.metaweather.com/api/location/search/?query=" + str(input("Podaj miasto po engilesku: ").lower())
url = "https://www.metaweather.com/api/location/search/?query=warsaw"
response = requests.get(url)
url2 = "https://www.metaweather.com/api/location/" + str(response.json()[0]["woeid"]) + "/"
response2 = requests.get(url2)
print("Aktualna temperatura:", response2.json()['consolidated_weather'][0]['the_temp'])
print("Ciśnienie:", response2.json()['consolidated_weather'][0]['air_pressure'])
print("Wilgotność:", response2.json()['consolidated_weather'][0]['humidity'])