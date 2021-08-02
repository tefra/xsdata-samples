from dataclasses import dataclass, field
from .family_facility_enumeration import FamilyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FamilyFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FamilyFacilityEnumeration = field(
        default=FamilyFacilityEnumeration.NONE,
        metadata={
            "required": True,
        }
    )
