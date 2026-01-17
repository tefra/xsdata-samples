from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VmsDatexSupplementalPictogramEnum(Enum):
    """
    Types of pictograms displayable in supplementary panels (normally below
    the main pictogram display which it qualifies).

    :cvar DISTANCE_TO_THE_BEGINNINGOF_THE_APPLICATION_ZONE: Distance to
        the beginning of the application zone.
    :cvar EXCEPT_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER: Except any
        power driven vehicle drawing a trailer.
    :cvar EXCEPT_BUS: Except for buses.
    :cvar EXCEPT_GOODS_VEHICLES: Except for goods vehicles.
    :cvar EXCEPT_SEMI_TRAILER: Except for semi trailers (i.e. any
        trailer designed to be coupled to a motor vehicle in such a way
        that part of its weight and that of its load is borne by the
        motor vehicle).
    :cvar EXCEPT_VEHICLES_CARRYING_DANGEROUS_GOODS: Except for vehicles
        carrying dangerous goods (i.e. for which special sign plating is
        prescribed).
    :cvar IN_CASE_OF_ICE_OR_SNOW: In case of ice or snow.
    :cvar LENGTH_OF_THE_APPLICATION_ZONE: Length of the applicable zone.
    :cvar RESTRICTED_TO_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER:
        Restricted to any power driven vehicle drawing a trailer.
    :cvar RESTRICETD_TO_BUS: Restricted to buses.
    :cvar RESTRICTED_TO_GOODS_VEHICLES: Restricted to goods vehicles.
    :cvar RESTRICTED_TO_SEMI_TRAILER: Restricted to semi trailers (i.e.
        any trailer designed to be coupled to a motor vehicle in such a
        way that part of its wieght and that of its load is borne by the
        motor vehicle).
    :cvar RESTRICTED_TO_VEHICLES_CARRYING_DANGEROUS_GOODS: Restricted to
        vehicles carrying dangerous goods (i.e. for which special sign
        plating is prescribed).
    :cvar MAINTENANCE_VEHICLES: Maintenance vehicles.
    :cvar SNOW_PLOUGHS: Snow ploughs.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    DISTANCE_TO_THE_BEGINNINGOF_THE_APPLICATION_ZONE = (
        "distanceToTheBeginningofTheApplicationZone"
    )
    EXCEPT_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER = (
        "exceptAnyPowerDrivenVehicleDrawingTrailer"
    )
    EXCEPT_BUS = "exceptBus"
    EXCEPT_GOODS_VEHICLES = "exceptGoodsVehicles"
    EXCEPT_SEMI_TRAILER = "exceptSemiTrailer"
    EXCEPT_VEHICLES_CARRYING_DANGEROUS_GOODS = (
        "exceptVehiclesCarryingDangerousGoods"
    )
    IN_CASE_OF_ICE_OR_SNOW = "inCaseOfIceOrSnow"
    LENGTH_OF_THE_APPLICATION_ZONE = "lengthOfTheApplicationZone"
    RESTRICTED_TO_ANY_POWER_DRIVEN_VEHICLE_DRAWING_TRAILER = (
        "restrictedToAnyPowerDrivenVehicleDrawingTrailer"
    )
    RESTRICETD_TO_BUS = "restricetdToBus"
    RESTRICTED_TO_GOODS_VEHICLES = "restrictedToGoodsVehicles"
    RESTRICTED_TO_SEMI_TRAILER = "restrictedToSemiTrailer"
    RESTRICTED_TO_VEHICLES_CARRYING_DANGEROUS_GOODS = (
        "restrictedToVehiclesCarryingDangerousGoods"
    )
    MAINTENANCE_VEHICLES = "maintenanceVehicles"
    SNOW_PLOUGHS = "snowPloughs"
    OTHER = "other"
