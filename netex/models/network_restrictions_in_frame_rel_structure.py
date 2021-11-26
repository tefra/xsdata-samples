from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .meeting_restriction import MeetingRestriction
from .overtaking_possibility import OvertakingPossibility
from .restricted_manoeuvre import RestrictedManoeuvre
from .vehicle_type_at_point import VehicleTypeAtPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkRestrictionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "networkRestrictionsInFrame_RelStructure"

    overtaking_possibility: List[OvertakingPossibility] = field(
        default_factory=list,
        metadata={
            "name": "OvertakingPossibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    meeting_restriction: List[MeetingRestriction] = field(
        default_factory=list,
        metadata={
            "name": "MeetingRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restricted_manoeuvre: List[RestrictedManoeuvre] = field(
        default_factory=list,
        metadata={
            "name": "RestrictedManoeuvre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_at_point: List[VehicleTypeAtPoint] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeAtPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
