from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VehicleTypeEnum(Enum):
    """
    Types of vehicle.

    :cvar AGRICULTURAL_VEHICLE: Vehicle normally used for agricultural
        purposes, e.g. tractor, combined harvester etc.
    :cvar ANY_VEHICLE: Vehicle of any type.
    :cvar ARTICULATED_VEHICLE: Articulated vehicle.
    :cvar BICYCLE: Bicycle.
    :cvar BUS: Bus.
    :cvar CAR: Car.
    :cvar CARAVAN: Caravan.
    :cvar CAR_OR_LIGHT_VEHICLE: Car or light vehicle.
    :cvar CAR_WITH_CARAVAN: Car towing a caravan.
    :cvar CAR_WITH_TRAILER: Car towing a trailer.
    :cvar CONSTRUCTION_OR_MAINTENANCE_VEHICLE: Vehicle normally used for
        construction or maintenance purposes, e.g. digger, excavator,
        bulldozer, lorry mounted crane etc.
    :cvar FOUR_WHEEL_DRIVE: Four wheel drive vehicle.
    :cvar HIGH_SIDED_VEHICLE: High sided vehicle.
    :cvar LORRY: Lorry of any type.
    :cvar MOPED: Moped (a two wheeled motor vehicle characterized by a
        small engine typically less than 50cc and by normally having
        pedals).
    :cvar MOTORCYCLE: Motorcycle.
    :cvar MOTORCYCLE_WITH_SIDE_CAR: Three wheeled vehicle comprising a
        motorcycle with an attached side car.
    :cvar MOTORSCOOTER: Motorscooter (a two wheeled motor vehicle
        characterized by a step-through frame and small diameter
        wheels).
    :cvar TANKER: Vehicle with large tank for carrying bulk liquids.
    :cvar THREE_WHEELED_VEHICLE: Three wheeled vehicle of unspecified
        type.
    :cvar TRAILER: Trailer.
    :cvar TRAM: Tram.
    :cvar TWO_WHEELED_VEHICLE: Two wheeled vehicle of unspecified type.
    :cvar VAN: Van.
    :cvar VEHICLE_WITH_CATALYTIC_CONVERTER: Vehicle with catalytic
        converter.
    :cvar VEHICLE_WITHOUT_CATALYTIC_CONVERTER: Vehicle without catalytic
        converter.
    :cvar VEHICLE_WITH_CARAVAN: Vehicle (of unspecified type) towing a
        caravan.
    :cvar VEHICLE_WITH_TRAILER: Vehicle (of unspecified type) towing a
        trailer.
    :cvar WITH_EVEN_NUMBERED_REGISTRATION_PLATES: Vehicle with even
        numbered registration plate.
    :cvar WITH_ODD_NUMBERED_REGISTRATION_PLATES: Vehicle with odd
        numbered registration plate.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    AGRICULTURAL_VEHICLE = "agriculturalVehicle"
    ANY_VEHICLE = "anyVehicle"
    ARTICULATED_VEHICLE = "articulatedVehicle"
    BICYCLE = "bicycle"
    BUS = "bus"
    CAR = "car"
    CARAVAN = "caravan"
    CAR_OR_LIGHT_VEHICLE = "carOrLightVehicle"
    CAR_WITH_CARAVAN = "carWithCaravan"
    CAR_WITH_TRAILER = "carWithTrailer"
    CONSTRUCTION_OR_MAINTENANCE_VEHICLE = "constructionOrMaintenanceVehicle"
    FOUR_WHEEL_DRIVE = "fourWheelDrive"
    HIGH_SIDED_VEHICLE = "highSidedVehicle"
    LORRY = "lorry"
    MOPED = "moped"
    MOTORCYCLE = "motorcycle"
    MOTORCYCLE_WITH_SIDE_CAR = "motorcycleWithSideCar"
    MOTORSCOOTER = "motorscooter"
    TANKER = "tanker"
    THREE_WHEELED_VEHICLE = "threeWheeledVehicle"
    TRAILER = "trailer"
    TRAM = "tram"
    TWO_WHEELED_VEHICLE = "twoWheeledVehicle"
    VAN = "van"
    VEHICLE_WITH_CATALYTIC_CONVERTER = "vehicleWithCatalyticConverter"
    VEHICLE_WITHOUT_CATALYTIC_CONVERTER = "vehicleWithoutCatalyticConverter"
    VEHICLE_WITH_CARAVAN = "vehicleWithCaravan"
    VEHICLE_WITH_TRAILER = "vehicleWithTrailer"
    WITH_EVEN_NUMBERED_REGISTRATION_PLATES = (
        "withEvenNumberedRegistrationPlates"
    )
    WITH_ODD_NUMBERED_REGISTRATION_PLATES = "withOddNumberedRegistrationPlates"
    OTHER = "other"
