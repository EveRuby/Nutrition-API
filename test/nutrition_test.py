from app.nutrition_API_Main import fetch_nutrition_info


from app.nutrition_API_Main import fetch_nutrition_info

def test_fetch_nutrition():
    result=fetch_nutrition_info("chicken soup")
    assert isinstance(result,dict)
    assert "calories" in list(result.keys())
    assert "fat" in list(result.keys())
    assert "recipesUsed" in list(result.keys())
    assert "protein" in list(result.keys())
    assert "carbs" in list(result.keys())
