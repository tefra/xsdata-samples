from dataclasses import dataclass, field
from typing import Optional

from .link_version_structure import LinkVersionStructure
from .operational_context_ref import OperationalContextRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .vehicle_mode import VehicleMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "ServiceLink_VersionStructure"

    from_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    vehicle_mode: VehicleMode | None = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_context_ref: OperationalContextRef | None = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
