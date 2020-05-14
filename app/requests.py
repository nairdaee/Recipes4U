
import requests
import urllib.request, json
from .models import  MealPlan, Joke, SearchIngredients

# Getting api key
api_key= "e7ba7ecc9faf4e32a68df8753b188959"
base_url = None    

SEARCH_MEALPLAN_URL = 'https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey=e7ba7ecc9faf4e32a68df8753b188959&includeNutrition=false'
JOKE_URL = "https://api.spoonacular.com/food/jokes/random?apiKey=e7ba7ecc9faf4e32a68df8753b188959"
SEARCH_RECIPES_BY_INGREDIENTS_url=None
GET_RECIPE_INFORMATION_url=None
def configure_request(app):
    global SEARCH_RECIPES_BY_INGREDIENTS_url,api_key,GET_RECIPE_INFORMATION_url,SEARCH_MEALPLAN_URL,JOKE_URL

    api_key=app.config['API_KEY']
    SEARCH_RECIPES_BY_INGREDIENTS_url=app.config['SEARCH_RECIPES_BY_INGREDIENTS']
    GET_RECIPE_INFORMATION_url=app.config['GET_RECIPE_INFORMATION']
    SEARCH_MEALPLAN_URL=app.config['SEARCH_MEALPLAN']
    JOKE_URL=app.config['JOKE_URL']
# SEARCHBY API CALL
def get_search_by_ingredients(ingredients):
    """
     Function that gets the json response to our url request
    """
    get_search_by_ingredients_url=SEARCH_RECIPES_BY_INGREDIENTS_url.format(ingredients,api_key)

    fetch=requests.get(get_search_by_ingredients_url)
    get_search_by_ingredients_response=fetch.json()

    # results=
    # print([obj.get('id') for obj in get_search_by_ingredients_response])
   
    
    # for recipe in get_search_by_ingredients_response:
    #     id =recipe.get("id",'default value')
    #     # print(recipe)

    return get_search_by_ingredients_response

def get_recipe_information(id):
    """
    Function that gets the json response to our url request
    """
    get_recipe_information_url=GET_RECIPE_INFORMATION_url.format(id,api_key)
    print(get_recipe_information_url)
    fetch=requests.get(get_recipe_information_url)
    get_recipe_information_response=fetch.json()
    print(get_recipe_information_response)

    return get_recipe_information_response
 
def get_mealplan(mealplan):
    """
    Function to consume http request and return a Mealplan class instance
    """
    get_mealplan_url= SEARCH_MEALPLAN_URL.format(mealplan,api_key)
    fetch=requests.get(get_mealplan_url)
    get_mealplan_response=fetch.json()
    
    return get_mealplan_response

def get_joke():
    """
    Function to consume http request and return a Mealplan class instance
    """
    response = requests.get(JOKE_URL).json()

    random_joke = Joke(response.get("text"))
    return random_joke


