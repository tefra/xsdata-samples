from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.dead_run_endpoint_structure import DeadRunEndpointStructure
from netex.models.dead_run_type_enumeration import DeadRunTypeEnumeration
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.group_of_services_refs_rel_structure import GroupOfServicesRefsRelStructure
from netex.models.line_ref import LineRef
from netex.models.operator_ref import OperatorRef
from netex.models.train_number_refs_rel_structure import TrainNumberRefsRelStructure
from netex.models.vehicle_journey_version_structure import VehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunVersionStructure(VehicleJourneyVersionStructure):
    class Meta:
        name = "DeadRun_VersionStructure"

    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_services: Optional[GroupOfServicesRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_numbers: Optional[TrainNumberRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    origin: Optional[DeadRunEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination: Optional[DeadRunEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_type: Optional[DeadRunTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeadRunType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
