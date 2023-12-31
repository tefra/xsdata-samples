from dataclasses import dataclass, field
from typing import Optional
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_meeting_point_ref import VehicleMeetingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleMeetingPointRefs_RelStructure"

    vehicle_meeting_point_ref: Optional[VehicleMeetingPointRef] = field(
        default=None,
        metadata={
            "name": "VehicleMeetingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
