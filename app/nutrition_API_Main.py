import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint
import sys

API_KEY = os.environ["API_KEY"]




def fetch_nutrition_info(recipe_title):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"

    querystring = {"title":recipe_title}
    headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
            }

    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed_response = json.loads(response.text)
    return parsed_response



def meal_plan(targetCalories_input, diet_input, exclude_input):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
        
    querystring = {"timeFrame":"day","targetCalories": targetCalories_input,"diet": diet_input,"exclude":exclude_input}

    headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed_response = json.loads(response.text)
    return parsed_response




if __name__ == '__main__':


    print("---------START----------")
    print("WELCOME TO YOUR MEAL PAL!")
    print("WHAT WOULD YOU LIKE TO DO?")
    print("A: Look up nutrition information")
    print("B: Generate a meal plan")


    task = input()


    if task.upper() == "A":
        
        print("------------------------")
        print("YOU CHOSE TO LOOK UP NUTRITION INFORMATION")
        print("------------------------")
            
        recipe=input("PLEASE ENTER THE NAME OF A RECIPE YOU WANT TO COOK AND HIT 'ENTER': ")
        parsed_response=fetch_nutrition_info(recipe)

        # url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition"

        # querystring = {"title":recipe}
        # headers = {
        #         'x-rapidapi-key': API_KEY,
        #         'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        #         }

        # response = requests.request("GET", url, headers=headers, params=querystring)
        # parsed_response = json.loads(response.text)
        if "calories" not in parsed_response.keys():
            print("****PLEASE ENTER A VALID RECIPE!!****")
            sys.exit()
        else:
            calories=int(parsed_response["calories"]["value"])
            fat=int(parsed_response["fat"]["value"])
            carbs=int(parsed_response["carbs"]["value"])
            protein=int(parsed_response["protein"]["value"])
            print("------------------------")
            print("NUTRITION INFORMATION FOR", recipe+":" )
            print("------------------------")
            print("CALORIES:", calories)
            print("PROTEIN: ", protein, "grams")
            print("FAT: ", fat, "grams")
            print("CARBOHYDRATES: ", carbs, "grams")
        

    elif task.upper() == "B":

        print("------------------------")
        print("GENERATE A MEAL PLAN WITH 3 SIMPLE QUESTIONS:")
        print("------------------------")

        #Getting user input
        targetCalories_input=input("-1- WHAT IS YOUR DAILY CALORIE TARGET (e.g. 2000)? Press ""ENTER"" to skip. ")
        diet_input = input("-2- PREFERRED DIET? Press ""ENTER"" to skip. ")
        exclude_input = input("-3- WHAT FOODS WOULD YOU LIKE TO EXCLUDE? Press ""ENTER"" to skip. ")

        #Converting empty strings to "None" values
        empty_string=str()
        conv = lambda i : None
        if targetCalories_input == empty_string:
            targetCalories_input = conv(targetCalories_input)
        if diet_input == empty_string:
            diet_input = conv(diet_input)
        if exclude_input == empty_string:
            exclude_input = conv(exclude_input)

        #Passing API parameters and getting a response
        # url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"
        
        # querystring = {"timeFrame":"day","targetCalories": targetCalories_input,"diet": diet_input,"exclude":exclude_input}

        # headers = {
        # 'x-rapidapi-key': API_KEY,
        # 'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        # }

        # response = requests.request("GET", url, headers=headers, params=querystring)


        #parsing and printing the response
        print("------------------------")
        print("YOUR SUGGESTED MEAL PLAN:")
        print("------------------------")
        
        
        # parsed_response = json.loads(response.text)
        parsed_response=meal_plan(targetCalories_input, diet_input, exclude_input)
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
        print("TOTAL DAILY NUTRITION:")
        print("------------------------")
        print("CALORIES:", total_cal)
        print("PROTEIN:", total_prot)
        print("FAT:", total_fat)
        print("CARBOHYDRATES:", total_carb)
        


    print("------------------------")
    print ("THANK YOU FOR USING MEAL PAL!")
    print("REMEMBER: EVERYTHING IS GOOD IN MODERATION, INCLUDING MODERATION  -- Oscar Wilde :)")
    print("-----------END----------")



#########################

