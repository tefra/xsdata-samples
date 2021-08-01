from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadsideServiceDisruptionTypeEnum(Enum):
    """
    Types of disruption to roadside services relevant to road users.

    :cvar BAR_CLOSED: Bar closed.
    :cvar DIESEL_SHORTAGE: There is a shortage of diesel at the
        specified location.
    :cvar FUEL_SHORTAGE: There is a shortage of fuel (of one or more
        types) at the specified location.
    :cvar LPG_SHORTAGE: There is a shortage of liquid petroleum gas at
        the specified location.
    :cvar METHANE_SHORTAGE: There is a shortage of methane at the
        specified location.
    :cvar NO_DIESEL_FOR_HEAVY_VEHICLES: There is no diesel available for
        heavy goods vehicles at the specified location.
    :cvar NO_DIESEL_FOR_LIGHT_VEHICLES: There is no diesel available for
        light vehicles at the specified location.
    :cvar NO_PUBLIC_TELEPHONES: There are no available public telephones
        at the specified location.
    :cvar NO_TOILET_FACILITIES: There are no available public toilet
        facilities at the specified location.
    :cvar NO_VEHICLE_REPAIR_FACILITIES: There are no available vehicle
        repair facilities at the specified location.
    :cvar PETROL_SHORTAGE: There is a shortage of petrol at the
        specified location.
    :cvar REST_AREA_BUSY: The rest area at the specified location is
        busy.
    :cvar REST_AREA_CLOSED: The rest area at the specified location is
        closed.
    :cvar REST_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_REST_AREA: The rest
        area at the specified location is close to capacity and
        motorists are advised to seek an alternative.
    :cvar SERVICE_AREA_BUSY: The service area at the specified location
        is close to capacity.
    :cvar SERVICE_AREA_CLOSED: The service area at the specified
        location is closed.
    :cvar SERVICE_AREA_FUEL_STATION_CLOSED: The fuel station at the
        specified service area is closed.
    :cvar SERVICE_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_SERVICE_AREA: The
        service area at the specified location is close to capacity and
        motorists are advised to seek an alternative.
    :cvar SERVICE_AREA_RESTAURANT_CLOSED: The restaurant at the
        specified service area is closed.
    :cvar SOME_COMMERCIAL_SERVICES_CLOSED: Some commercial services are
        closed at the specified location.
    :cvar WATER_SHORTAGE: There is a shortage of water at the specified
        location.
    """
    BAR_CLOSED = "barClosed"
    DIESEL_SHORTAGE = "dieselShortage"
    FUEL_SHORTAGE = "fuelShortage"
    LPG_SHORTAGE = "lpgShortage"
    METHANE_SHORTAGE = "methaneShortage"
    NO_DIESEL_FOR_HEAVY_VEHICLES = "noDieselForHeavyVehicles"
    NO_DIESEL_FOR_LIGHT_VEHICLES = "noDieselForLightVehicles"
    NO_PUBLIC_TELEPHONES = "noPublicTelephones"
    NO_TOILET_FACILITIES = "noToiletFacilities"
    NO_VEHICLE_REPAIR_FACILITIES = "noVehicleRepairFacilities"
    PETROL_SHORTAGE = "petrolShortage"
    REST_AREA_BUSY = "restAreaBusy"
    REST_AREA_CLOSED = "restAreaClosed"
    REST_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_REST_AREA = "restAreaOvercrowdedDriveToAnotherRestArea"
    SERVICE_AREA_BUSY = "serviceAreaBusy"
    SERVICE_AREA_CLOSED = "serviceAreaClosed"
    SERVICE_AREA_FUEL_STATION_CLOSED = "serviceAreaFuelStationClosed"
    SERVICE_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_SERVICE_AREA = "serviceAreaOvercrowdedDriveToAnotherServiceArea"
    SERVICE_AREA_RESTAURANT_CLOSED = "serviceAreaRestaurantClosed"
    SOME_COMMERCIAL_SERVICES_CLOSED = "someCommercialServicesClosed"
    WATER_SHORTAGE = "waterShortage"
