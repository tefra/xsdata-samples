from __future__ import annotations

from dataclasses import dataclass, field

from .link_version_structure import LinkVersionStructure
from .operational_context_ref import OperationalContextRef
from .timing_point_ref_structure import TimingPointRefStructure
from .vehicle_mode import VehicleMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "TimingLink_VersionStructure"

    from_point_ref: TimingPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_point_ref: TimingPointRefStructure | None = field(
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
