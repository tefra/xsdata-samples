from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplayViewsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "destinationDisplayViews_RelStructure"

    destination_display_ref: List[DestinationDisplayRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_view: List[DestinationDisplayView] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
