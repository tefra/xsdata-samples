from dataclasses import dataclass, field
from typing import List, Optional
from .line_section_point_type_enumeration import (
    LineSectionPointTypeEnumeration,
)
from .point_on_section_versioned_child_structure import (
    PointOnSectionVersionedChildStructure,
)
from .vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLineSectionVersionedChildStructure(
    PointOnSectionVersionedChildStructure
):
    class Meta:
        name = "PointOnLineSection_VersionedChildStructure"

    line_section_point_type: Optional[LineSectionPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LineSectionPointType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    show_as_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowAsAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connecting_vehicle_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingVehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
