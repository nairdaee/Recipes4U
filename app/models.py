class FoodVideos:
    def __init__(self,shortTitle,title,youTubeId, views):
        self.shortTitle = shortTitle
        self.title = title
        self.youTubeId = youTubeId
        self.views = views
class Recipe:
    '''
    Recipe class to define recipe objects
    '''

    def __init__(self,id,title,readyInMinutes,servings,sourceUrl,image):
        self.id = id
        self.title= title
        self.readyInMinutes = readyInMinutes
        self.servings = servings
        self.sourceUrl = sourceUrl
        self.image = image

class MealPlan:

    """
    Adds mealplan class derived from the Api
    """


    def __init__(self,id,title,readyInMinutes,servings,sourceUrl):
        self.id = id
        self.title = title
        self.readyInMinutes = readyInMinutes
        self.servings = servings
        self.sourceUrl = sourceUrl

class Joke:

    """
    Adds joke class derived from Api
    """

    def __init__(self,text):
        self.text = text
        
class SearchIngredients:
    """
    """

    def __init__(self,id,title,image):
        self.id=id
        self.title=title
        self.image=image

