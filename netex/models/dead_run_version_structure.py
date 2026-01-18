from __future__ import annotations

from dataclasses import dataclass, field

from .dead_run_endpoint_structure import DeadRunEndpointStructure
from .dead_run_type_enumeration import DeadRunTypeEnumeration
from .direction_type import DirectionType
from .flexible_line_ref import FlexibleLineRef
from .group_of_services_refs_rel_structure import (
    GroupOfServicesRefsRelStructure,
)
from .line_ref import LineRef
from .operator_ref import OperatorRef
from .train_number_refs_rel_structure import TrainNumberRefsRelStructure
from .vehicle_journey_version_structure import VehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunVersionStructure(VehicleJourneyVersionStructure):
    class Meta:
        name = "DeadRun_VersionStructure"

    operator_ref: None | OperatorRef = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_ref: None | FlexibleLineRef | LineRef = field(
        default=None,
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
            ),
        },
    )
    direction_type: None | DirectionType = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_services: None | GroupOfServicesRefsRelStructure = field(
        default=None,
        metadata={
            "name": "groupsOfServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_numbers: None | TrainNumberRefsRelStructure = field(
        default=None,
        metadata={
            "name": "trainNumbers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    origin: None | DeadRunEndpointStructure = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: None | DeadRunEndpointStructure = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dead_run_type: None | DeadRunTypeEnumeration = field(
        default=None,
        metadata={
            "name": "DeadRunType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
