from __future__ import annotations

from dataclasses import dataclass, field

from .parking_bay_status_enumeration import ParkingBayStatusEnumeration
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayStatusValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "ParkingBayStatus_ValueStructure"

    status: None | ParkingBayStatusEnumeration = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
