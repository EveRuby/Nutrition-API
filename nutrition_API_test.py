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

#{"recipesUsed":18,"calories":{"value":530.0,"unit":"calories","confidenceRange95Percent":{"min":446.62,"max":604.76},"standardDeviation":171.15},"fat":{"value":39.0,"unit":"g","confidenceRange95Percent":{"min":29.08,"max":44.13},"standardDeviation":16.28},"protein":{"value":22.0,"unit":"g","confidenceRange95Percent":{"min":19.42,"max":26.16},"standardDeviation":7.29},"carbs":{"value":28.0,"unit":"g","confidenceRange95Percent":{"min":20.85,"max":31.07},"standardDeviation":11.06}}

