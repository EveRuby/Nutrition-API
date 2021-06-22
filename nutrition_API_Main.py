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

    targetCalories_input=input("-1- WHAT IS YOUR DAILY CALORY TARGET (e.g. 2000)? Press ""ENTER"" to skip. ")
    diet_input = input("-2- PREFERED DIET? Press ""ENTER"" to skip. ")
    exclude_input = input("-3- WHAT FOODS WOULD YOU LIKE TO EXCLUDE? Press ""ENTER"" to skip. ")

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

    #querystring = {"timeFrame":"day","targetCalories": str(targetCalories_input),"diet": str(diet_input),"exclude":str(exclude_input)}

    #querystring = {"timeFrame":"day","targetCalories": None,"diet": None,"exclude": None}
    
    querystring = {"timeFrame":"day","targetCalories": targetCalories_input,"diet": str(diet_input),"exclude":str(exclude_input)}

    headers = {
    'x-rapidapi-key': "a5ce2f9e6emsh998846a2687ac6dp1f998fjsn61c08831d7df",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    #EXAMPLE RESPONSE: 
    #{'meals': [{'id': 1100990, 'imageType': 'jpg', 'title': 'Blueberry, Chocolate & Cocao Superfood Pancakes - Gluten-Free/Paleo/Vegan', 'readyInMinutes': 30, 'servings': 2, 'sourceUrl': 'https://spoonacular.com/blueberry-chocolate-cocao-superfood-pancakes-gluten-free-paleo-vegan-1100990'}, 
    
    #{'id': 81273, 'imageType': 'jpg', 'title': 'Beef Pot Roast', 'readyInMinutes': 20, 'servings': 4, 'sourceUrl': 'http://www.myrecipes.com/recipe/beef-pot-roast-10000000780316/'}, 
    
    #{'id': 478685, 'imageType': 'jpg', 'title': 'Grilled chicken marinated in coconut cream', 'readyInMinutes': 45, 'servings': 4, 'sourceUrl': 'http://feastasia.casaveneracion.com/grilled-chicken-marinated-in-coconut-cream/'}], 
    
    #'nutrients': {'calories': 1999.78, 'protein': 129.44, 'fat': 123.78, 'carbohydrates': 98.47}}

    print("------------------------")
    print("YOUR SUGGESTED MEAL PLAN:")
    print("------------------------")
    parsed_response = json.loads(response.text)
    breakfast=parsed_response["meals"][0]["title"]
    lunch=parsed_response["meals"][1]["title"]
    dinner=parsed_response["meals"][2]["title"]
    total_cal=parsed_response["nutrients"]["calories"]
    total_prot=parsed_response["nutrients"]["protein"]
    total_fat=parsed_response["nutrients"]["fat"]
    total_carb=parsed_response["nutrients"]["carbohydrates"]
    print("BREAKFAST:", breakfast)
    print("LUNCH:", lunch)
    print("DINNER:", dinner)
    print("------------------------")
    print("NUTRIOTION:")
    print("------------------------")
    print("TOTAL CALORIES:", total_cal)
    print("      PROTEIN:", total_prot)
    print("      FAT:", total_fat)
    print("      CARBOHYDRATES:", total_carb)
    print("------------------------")
    #print(parsed_response)

    #print(response.text)
    #print(type(response.text))


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
