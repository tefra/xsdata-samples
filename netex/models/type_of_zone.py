from dataclasses import dataclass
from netex.models.type_of_zone_value_structure import TypeOfZoneValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfZone(TypeOfZoneValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
