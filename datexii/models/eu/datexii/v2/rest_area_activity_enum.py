from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RestAreaActivityEnum(Enum):
    """
    Rest area activity enum.

    :cvar OPEN_FIRE: Open fire.
    :cvar OVERNIGHT_PARKING: Overnight parking.
    :cvar PICNIC: Picnic.
    :cvar SMOKING: Smoking.
    :cvar CAMPING: Camping.
    :cvar HANDLING_HAZARDOUS_MATERIAL: Handling with hazardous material.
    :cvar BARBECUE: Barbeque.
    :cvar OTHER: Other.
    """
    OPEN_FIRE = "openFire"
    OVERNIGHT_PARKING = "overnightParking"
    PICNIC = "picnic"
    SMOKING = "smoking"
    CAMPING = "camping"
    HANDLING_HAZARDOUS_MATERIAL = "handlingHazardousMaterial"
    BARBECUE = "barbecue"
    OTHER = "other"
