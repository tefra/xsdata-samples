from dataclasses import dataclass
from netex.models.type_of_facility_version_structure import TypeOfFacilityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFacility(TypeOfFacilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
