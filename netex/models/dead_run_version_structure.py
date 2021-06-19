from dataclasses import dataclass, field
from typing import List, Optional
from .dead_run_endpoint_structure import DeadRunEndpointStructure
from .dead_run_type_enumeration import DeadRunTypeEnumeration
from .direction_type_enumeration import DirectionTypeEnumeration
from .flexible_line_ref import FlexibleLineRef
from .group_of_services_refs_rel_structure import GroupOfServicesRefsRelStructure
from .line_ref import LineRef
from .operator_ref import OperatorRef
from .train_number_refs_rel_structure import TrainNumberRefsRelStructure
from .vehicle_journey_version_structure import VehicleJourneyVersionStructure

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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionType",
                    "type": DirectionTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfServices",
                    "type": GroupOfServicesRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "trainNumbers",
                    "type": TrainNumberRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Origin",
                    "type": DeadRunEndpointStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Destination",
                    "type": DeadRunEndpointStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunType",
                    "type": DeadRunTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 10,
        }
    )
