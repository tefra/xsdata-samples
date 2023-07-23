from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeMealService(Enum):
    """
    Available Meal Service.
    """
    MEAL = "Meal"
    COLD_MEAL = "ColdMeal"
    HOT_MEAL = "HotMeal"
    BREAKFAST = "Breakfast"
    CONTINENTAL_BREAKFAST = "ContinentalBreakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACK_OR_BRUNCH = "SnackOrBrunch"
    FOOD_FOR_PURCHASE = "FoodForPurchase"
    COMPLIMENTARY_REFRESHMENTS = "ComplimentaryRefreshments"
    ALCOHOLIC_BEVERAGES_FOR_PURCHASE = "AlcoholicBeveragesForPurchase"
    COMPLIMENTARY_ALCOHOLIC_BEVERAGES = "ComplimentaryAlcoholicBeverages"
    FOOD_AND_BEVERAGES_FOR_PURCHASE = "FoodAndBeveragesForPurchase"
    NO_MEAL_SERVICE = "NoMealService"
    REFRESHMENTS_FOR_PURCHASE = "RefreshmentsForPurchase"
