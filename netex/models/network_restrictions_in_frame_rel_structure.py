from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .infrastructure_link_restriction import InfrastructureLinkRestriction
from .meeting_restriction import MeetingRestriction
from .network_restriction import NetworkRestriction
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
    infrastructure_link_restriction: List[InfrastructureLinkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLinkRestriction",
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
    network_restriction: List[NetworkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "NetworkRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
