import requests
import json


# product_ids=[]
# for p in products1:
#     product_ids.append(str(p["id"]))

# selected_ids=[]
# while True:
#     selected_id = input("Please enter a product identifier and hit 'enter'; write 'DONE' when there are no more items: ")
#     if selected_id.upper() == "DONE":
#         break
#     else:
#         if str(selected_id) in product_ids:
#             selected_id=str(selected_id)
#             selected_ids.append(selected_id)
#         else:
#             print("That ID is not valid, please enter another.")
# print("-------------")
# print("NORA'S GROCERY")
# now= datetime.datetime.now()
# now_formatted=now.strftime("%Y-%m-%d %H:%M:%S %p")
# print("CHECKOUT AT:", now_formatted)
# print("-------------")
# if len(selected_ids)==0:
#     print("No Items")
# else:
#     print("SELECTED PRODUCTS:")

##ideally we will create a dictionary and store each item below in its own key


print("WELCOME TO YOUR MEAL PAL!")
print("WHAT WOULD YOU LIKE TO DO?")
print("A: Look up nutrition information")
print("B: Generate a meal plan")
print("C: Find a recipe")


task = input()

if task == "A":
    
    print("YOU CHOSE TO LOOK UP NUTRIOTION INFORMATION")
    
    nutrition={}
    calories_input=input("Please enter the number of calories per day:")
    nutrition["calories"]=calories_input
    fat_input=input("Please enter the number of grams of fat per day:")
    nutrition["fat"]=fat_input
    carbs_input=input("Please enter the number of grams of carbohydrates per day:")
    nutrition["carbs"]=carbs_input
    print(nutrition)

    recipe=input("Please enter the name of a recipe you want to cook and hit 'enter'; write 'Done' when you have entered recipes for the day: ")

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"

    querystring = {"title":"recipe"}
    headers = {
        'x-rapidapi-key': "a5ce2f9e6emsh998846a2687ac6dp1f998fjsn61c08831d7df",
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed_response = json.loads(response.text)
    calories=int(parsed_response["calories"]["value"])
    print("The calories in your recipe are:", calories)
    print(parsed_response)
 



if task == "B":

    print("GENERATE A MEAL PLAN WITH 3 SIMPLE QUESTIONS:")
    
    meal_plan={}

    #Parameters: querystring = {"timeFrame":"day","targetCalories":"2000","diet":"vegetarian","exclude":"shellfish, olives"}

    target_calories=input("-1- WHAT IS YOUR DAILY CALORY TARGET (e.g. 2000)? Press ""ENTER"" to skip. ")
    diet = input("-2- PREFERED DIET? Press ""ENTER"" to skip. ")
    exclude = input("-3- WHAT FOODS WOULD YOU LIKE TO EXCLUDE? Press ""ENTER"" to skip. ")

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

    querystring = {"timeFrame":"day","targetCalories":"2000","diet":"vegetarian","exclude":"shellfish, olives"}

    headers = {
    'x-rapidapi-key': "a5ce2f9e6emsh998846a2687ac6dp1f998fjsn61c08831d7df",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    print(type(response.text))


if task == "C":
    print("YOU CHOSE TO FIND A RECIPE")





#     selected_id = input("Please enter a product identifier and hit 'enter'; write 'DONE' when there are no more items: ")
#     if selected_id.upper() == "DONE":
#         break
#     else:
#         if str(selected_id) in product_ids:
#             selected_id=str(selected_id)
#             selected_ids.append(selected_id)
#         else:
#             print("That ID is not valid, please enter another.")
