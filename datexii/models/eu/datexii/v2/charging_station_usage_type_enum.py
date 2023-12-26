from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ChargingStationUsageTypeEnum(Enum):
    """
    Type of usage for electric charging station(s).

    :cvar ELECTRIC_VEHICLE: Charging of electric vehicles.
    :cvar MOTORHOME_OR_CARAVAN_SUPPLY: Supply for motorhomes or
        caravans.
    :cvar ELECTRIC_BIKE_OR_MOTORCYCLE: Charging of E-Bikes or
        E-Motorcycles.
    :cvar LORRY_POWER_CONSUMPTION: Supply for lorries with power
        consumption, e.g. for refrigerated goods transports.
    :cvar ELECTRICAL_DEVICES: Provides a plug for electrical devices
        (e.g. shaver, mobile phones, hair dryer, ...)
    :cvar OTHER: Other usage for the electric charging stations.
    """

    ELECTRIC_VEHICLE = "electricVehicle"
    MOTORHOME_OR_CARAVAN_SUPPLY = "motorhomeOrCaravanSupply"
    ELECTRIC_BIKE_OR_MOTORCYCLE = "electricBikeOrMotorcycle"
    LORRY_POWER_CONSUMPTION = "lorryPowerConsumption"
    ELECTRICAL_DEVICES = "electricalDevices"
    OTHER = "other"
