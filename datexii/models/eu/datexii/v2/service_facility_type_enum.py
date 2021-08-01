from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ServiceFacilityTypeEnum(Enum):
    """Service facilities available on the parking site, parking space or group
    of parking spaces.

    In distinction to equipment, a service is mostly manned.

    :cvar HOTEL: A hotel.
    :cvar MOTEL: Hotel on the motorway or other accommodation service.
    :cvar OVERNIGHT_ACCOMMODATION: OvernightAccomodation.
    :cvar SHOP: A shop of unspecified kind.
    :cvar KIOSK: Kiosk.
    :cvar FOOD_SHOPPING: Food shopping.
    :cvar CAFE: Cafe.
    :cvar RESTAURANT: Restaurant.
    :cvar RESTAURANT_SELF_SERVICE: A restaurant where people arange and
        fetch their meal themselve, this might enclose a buffet.
    :cvar MOTORWAY_RESTAURANT: Restaurant located on a motorway rest
        area.
    :cvar MOTORWAY_RESTAURANT_SMALL: Smaller type of restaurant located
        on a motorway rest area. Might be with limited offers.
    :cvar SPARE_PARTS_SHOPPING: Spare parts shopping.
    :cvar PETROL_STATION: Indicates whether it is possible to get
        petrol.
    :cvar VEHICLE_MAINTENANCE: Garage repair service.
    :cvar TYRE_REPAIR: A tyre repair service.
    :cvar TRUCK_REPAIR: Truck repair.
    :cvar TRUCK_WASH: Truck wash.
    :cvar CAR_WASH: Car wash.
    :cvar PHARMACY: Pharmacy.
    :cvar MEDICAL_FACILITY: Medical facility.
    :cvar POLICE: Indicates whether a police station is on site or very
        close.
    :cvar TOURIST_INFORMATION: Tourist information with employees.
    :cvar BIKE_SHARING: Bike Sharing.
    :cvar DOCSTOP: The site is part of the Docstop project,
        http://www.docstoponline.eu, which means medical assistance for
        professional drivers.
    :cvar LAUNDRY: A possibility for washing clothes (might also be a
        laundromat with coins).
    :cvar LEISURE_ACTIVITIES: There are leisure activities offered on
        the site or in the very near surrounding. Use the additional
        description attribute to give details.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Some other service facility. Use
        'otherEquipmentOrServiceFacility' to specify it.
    """
    HOTEL = "hotel"
    MOTEL = "motel"
    OVERNIGHT_ACCOMMODATION = "overnightAccommodation"
    SHOP = "shop"
    KIOSK = "kiosk"
    FOOD_SHOPPING = "foodShopping"
    CAFE = "cafe"
    RESTAURANT = "restaurant"
    RESTAURANT_SELF_SERVICE = "restaurantSelfService"
    MOTORWAY_RESTAURANT = "motorwayRestaurant"
    MOTORWAY_RESTAURANT_SMALL = "motorwayRestaurantSmall"
    SPARE_PARTS_SHOPPING = "sparePartsShopping"
    PETROL_STATION = "petrolStation"
    VEHICLE_MAINTENANCE = "vehicleMaintenance"
    TYRE_REPAIR = "tyreRepair"
    TRUCK_REPAIR = "truckRepair"
    TRUCK_WASH = "truckWash"
    CAR_WASH = "carWash"
    PHARMACY = "pharmacy"
    MEDICAL_FACILITY = "medicalFacility"
    POLICE = "police"
    TOURIST_INFORMATION = "touristInformation"
    BIKE_SHARING = "bikeSharing"
    DOCSTOP = "docstop"
    LAUNDRY = "laundry"
    LEISURE_ACTIVITIES = "leisureActivities"
    UNKNOWN = "unknown"
    OTHER = "other"
