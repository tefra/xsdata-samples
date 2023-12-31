from dataclasses import dataclass, field
from typing import Optional
from .parking_bay_status_enumeration import ParkingBayStatusEnumeration
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayStatusValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "ParkingBayStatus_ValueStructure"

    status: Optional[ParkingBayStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
