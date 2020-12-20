import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/extract"

querystring = {"url":"http://www.melskitchencafe.com/the-best-fudgy-brownies/"}

headers = {
    'x-rapidapi-key': "40f738febfmsh8cb2be57094b599p10d15fjsn99576bbf8743",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
