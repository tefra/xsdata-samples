from dataclasses import dataclass, field
from typing import List
from .alternative_texts_rel_structure import (
    DayType,
    FareDayType,
    OrganisationDayType,
)
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dayTypesInFrame_RelStructure"

    fare_day_type: List[FareDayType] = field(
        default_factory=list,
        metadata={
            "name": "FareDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_day_type: List[OrganisationDayType] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationDayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type: List[DayType] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
