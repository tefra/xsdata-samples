from dataclasses import dataclass, field
from .reserved_space_facility_enumeration import (
    ReservedSpaceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReservedSpaceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ReservedSpaceFacilityEnumeration = field(
        default=ReservedSpaceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
