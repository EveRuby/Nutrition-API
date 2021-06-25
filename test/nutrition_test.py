from app.nutrition_API_Main import fetch_nutrition_info
from app.nutrition_API_Main import meal_plan

def test_fetch_nutrition():
    result=fetch_nutrition_info("chicken soup")
    assert isinstance(result,dict)
    assert "calories" in list(result.keys())
    assert "fat" in list(result.keys())
    assert "recipesUsed" in list(result.keys())
    assert "protein" in list(result.keys())
    assert "carbs" in list(result.keys())

def test_meal_plan():
    result=meal_plan(2000,"vegetarian","dairy")
    assert isinstance(result,dict)
    assert "nutrients" in list(result.keys())
    assert "meals" in list(result.keys())
    assert "readyInMinutes" in list(result["meals"][0].keys())
    assert "calories" in list(result["nutrients"].keys())
    assert "fat" in list(result["nutrients"].keys())
    assert "carbohydrates" in list(result["nutrients"].keys())
    assert "protein" in list(result["nutrients"].keys())
