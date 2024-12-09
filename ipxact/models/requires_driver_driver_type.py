from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class RequiresDriverDriverType(Enum):
    CLOCK = "clock"
    SINGLE_SHOT = "singleShot"
    ANY = "any"
