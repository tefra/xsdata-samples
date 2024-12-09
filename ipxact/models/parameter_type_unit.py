from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class ParameterTypeUnit(Enum):
    SECOND = "second"
    AMPERE = "ampere"
    KELVIN = "kelvin"
    HERTZ = "hertz"
    JOULE = "joule"
    WATT = "watt"
    COULOMB = "coulomb"
    VOLT = "volt"
    FARAD = "farad"
    OHM = "ohm"
    SIEMENS = "siemens"
    HENRY = "henry"
    CELSIUS = "Celsius"
