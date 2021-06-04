from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.infrastructure_link_restriction import InfrastructureLinkRestriction
from netex.models.meeting_restriction import MeetingRestriction
from netex.models.network_restriction import NetworkRestriction
from netex.models.overtaking_possibility import OvertakingPossibility
from netex.models.restricted_manoeuvre import RestrictedManoeuvre
from netex.models.vehicle_type_at_point import VehicleTypeAtPoint

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
            "min_occurs": 1,
        }
    )
    meeting_restriction: List[MeetingRestriction] = field(
        default_factory=list,
        metadata={
            "name": "MeetingRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    restricted_manoeuvre: List[RestrictedManoeuvre] = field(
        default_factory=list,
        metadata={
            "name": "RestrictedManoeuvre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    infrastructure_link_restriction: List[InfrastructureLinkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureLinkRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_type_at_point: List[VehicleTypeAtPoint] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeAtPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    network_restriction: List[NetworkRestriction] = field(
        default_factory=list,
        metadata={
            "name": "NetworkRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
