from dataclasses import dataclass
from .fare_unit_ref_structure import FareUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitRefStructure(FareUnitRefStructure):
    pass
