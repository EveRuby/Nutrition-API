import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"

querystring = {"title":"egg benedict"}

headers = {
    'x-rapidapi-key': "a5ce2f9e6emsh998846a2687ac6dp1f998fjsn61c08831d7df",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
print(type(response.text))

#{"recipesUsed":18,"calories":

