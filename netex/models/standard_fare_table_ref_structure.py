from dataclasses import dataclass

from .fare_table_ref_structure import FareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StandardFareTableRefStructure(FareTableRefStructure):
    pass
