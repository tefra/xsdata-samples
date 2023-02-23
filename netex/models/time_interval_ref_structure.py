from dataclasses import dataclass
from .fare_interval_ref_structure import FareIntervalRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalRefStructure(FareIntervalRefStructure):
    pass
