from dataclasses import dataclass
from netex.models.day_type_ref_structure import DayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypeRef(DayTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
