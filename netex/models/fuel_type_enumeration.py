from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FuelTypeEnumeration(Enum):
    BATTERY = "battery"
    BIODIESEL = "biodiesel"
    DIESEL = "diesel"
    DIESEL_BATTERY_HYBRID = "dieselBatteryHybrid"
    ELECTRIC_CONTACT = "electricContact"
    ELECTRICITY = "electricity"
    ETHANOL = "ethanol"
    HYDROGEN = "hydrogen"
    LIQUID_GAS = "liquidGas"
    TPG = "tpg"
    METHANE = "methane"
    NATURAL_GAS = "naturalGas"
    PETROL = "petrol"
    PETROL_BATTERY_HYBRID = "petrolBatteryHybrid"
    PETROL_LEADED = "petrolLeaded"
    PETROL_UNLEADED = "petrolUnleaded"
    NONE = "none"
    OTHER = "other"
