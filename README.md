# Meal Pal by Eve, Pegah, Rachel, Nora - NYU 2021
The Meal Pal app uses the Nutrition API and allows you to look up the nutrition information for a specific recipe and get a meal plan based on calorie input and specific diet.  The recipes come from the spoonable website- some examples include "chicken soup," "eggs benedict," "lasagna."


## Installation
Install the Meal Pal file from [Github](https://github.com/EveRuby/Nutrition-API.git)

## Create a Virtual Environment
Run in bash:
```bash
conda create -n meal_pal python=3.8
conda activate  meal_pal
pip install -r requirements.txt # (after specifying desired packages inside)
```

## API Key:
To use Meal Pal you must get an API Key from https://rapidapi.com/spoonacular/api/recipe-food-nutrition/.  Create a .env file and add a variable "API_KEY" with your API Key value.


Once the envioronment is created navigate to the folder with the downloaded nutrition_API_Main.py file

The API Key is only good for 50 requests per day.

## Run nutrition_API_Main.py File
```bash
python nutrition_API_Main.py
```
