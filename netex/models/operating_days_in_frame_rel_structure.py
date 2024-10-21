from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import OperatingDay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingDaysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "operatingDaysInFrame_RelStructure"

    operating_day: Iterable[OperatingDay] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
