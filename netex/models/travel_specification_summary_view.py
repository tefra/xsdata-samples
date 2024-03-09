from dataclasses import dataclass

from .travel_specification_summary_view_structure import (
    TravelSpecificationSummaryViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationSummaryView(TravelSpecificationSummaryViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
