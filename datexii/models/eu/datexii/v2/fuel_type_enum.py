from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class FuelTypeEnum(Enum):
    """
    Type of fuel used by a vehicle.

    :cvar BATTERY: Battery.
    :cvar BIODIESEL: Biodiesel.
    :cvar DIESEL: Diesel.
    :cvar DIESEL_BATTERY_HYBRID: Diesel and battery hybrid.
    :cvar ETHANOL: Ethanol.
    :cvar HYDROGEN: Hydrogen.
    :cvar LIQUID_GAS: Liquid gas of any type including LPG.
    :cvar LPG: Liquid petroleum gas.
    :cvar METHANE: Methane gas.
    :cvar PETROL: Petrol.
    :cvar PETROL_BATTERY_HYBRID: Petrol and battery hybrid.
    """

    BATTERY = "battery"
    BIODIESEL = "biodiesel"
    DIESEL = "diesel"
    DIESEL_BATTERY_HYBRID = "dieselBatteryHybrid"
    ETHANOL = "ethanol"
    HYDROGEN = "hydrogen"
    LIQUID_GAS = "liquidGas"
    LPG = "lpg"
    METHANE = "methane"
    PETROL = "petrol"
    PETROL_BATTERY_HYBRID = "petrolBatteryHybrid"
