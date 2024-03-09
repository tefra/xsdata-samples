from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import (
    DayType1,
    FareDayType,
    OrganisationDayType,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dayTypesInFrame_RelStructure"

    day_type: List[Union[FareDayType, OrganisationDayType, DayType1]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayType",
                    "type": FareDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationDayType",
                    "type": OrganisationDayType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayType",
                    "type": DayType1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
