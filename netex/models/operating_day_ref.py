from dataclasses import dataclass
from .operating_day_ref_structure import OperatingDayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDayRef(OperatingDayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
