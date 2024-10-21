from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking import Parking

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingsInFrame_RelStructure"

    parking: Iterable[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
