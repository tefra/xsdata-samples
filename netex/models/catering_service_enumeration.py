from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CateringServiceEnumeration(Enum):
    BAR = "bar"
    BEVERAGE_VENDING_MACHINE = "beverageVendingMachine"
    BUFFET = "buffet"
    COFFEE_SHOP = "coffeeShop"
    FIRST_CLASS_RESTAURANT = "firstClassRestaurant"
    FOOD_VENDING_MACHINE = "foodVendingMachine"
    HOT_FOOD_SERVICE = "hotFoodService"
    RESTAURANT = "restaurant"
    SNACKS = "snacks"
    TROLLEY_SERVICE = "trolleyService"
    NO_BEVERAGES_AVAILABLE = "noBeveragesAvailable"
    NO_FOOD_SERVICE_AVAILABLE = "noFoodServiceAvailable"
    OTHER = "other"
