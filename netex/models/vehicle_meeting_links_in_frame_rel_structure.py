from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_link import VehicleMeetingLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleMeetingLinksInFrame_RelStructure"

    vehicle_meeting_link: Iterable[VehicleMeetingLink] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
