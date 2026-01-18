from __future__ import annotations

from dataclasses import dataclass, field

from .all_modes_enumeration import AllModesEnumeration
from .authority_ref import AuthorityRef
from .operator_ref import OperatorRef
from .point_ref_structure import PointRefStructure
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .submode import Submode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConnectionEndStructure:
    transport_mode: AllModesEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    submode: Submode | None = field(
        default=None,
        metadata={
            "name": "Submode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_organisation_ref: AuthorityRef | OperatorRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    scheduled_stop_point_ref_or_vehicle_meeting_point_ref: (
        ScheduledStopPointRefStructure | PointRefStructure | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointRef",
                    "type": PointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
