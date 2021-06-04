from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TypeOfFuelEnumeration(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    NATURAL_GAS = "naturalGas"
    BIODIESEL = "biodiesel"
    ELECTRICITY = "electricity"
    OTHER = "other"
