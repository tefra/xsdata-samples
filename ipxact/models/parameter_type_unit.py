from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class ParameterTypeUnit(StrEnum):
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
