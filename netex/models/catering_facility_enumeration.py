from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CateringFacilityEnumeration(Enum):
    BAR = "bar"
    BISTRO = "bistro"
    BUFFET = "buffet"
    NO_FOOD_AVAILABLE = "noFoodAvailable"
    NO_BEVERAGES_AVAILABLE = "noBeveragesAvailable"
    RESTAURANT = "restaurant"
    FIRST_CLASS_RESTAURANT = "firstClassRestaurant"
    TROLLEY = "trolley"
    COFFEE_SHOP = "coffeeShop"
    HOT_FOOD_SERVICE = "hotFoodService"
    SELF_SERVICE = "selfService"
    SNACKS = "snacks"
    FOOD_VENDING_MACHINE = "foodVendingMachine"
    BEVERAGE_VENDING_MACHINE = "beverageVendingMachine"
    MINI_BAR = "miniBar"
    BREAKFAST_IN_CAR = "breakfastInCar"
    MEAL_AT_SEAT = "mealAtSeat"
    OTHER = "other"
    UNKNOWN = "unknown"
