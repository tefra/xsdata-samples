from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TypeOfCouplingEnumeration(Enum):
    SERVICE_FACILITY = "serviceFacility"
    COUPLING = "coupling"
    TARIFF_SECTION = "tariffSection"
    UNCOUPLED = "uncoupled"
