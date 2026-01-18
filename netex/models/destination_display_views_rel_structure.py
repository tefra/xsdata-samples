from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplayViewsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "destinationDisplayViews_RelStructure"

    destination_display_ref_or_destination_display_view: Iterable[
        DestinationDisplayRef | DestinationDisplayView
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
