from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import (
    DayType,
    FareDayType,
    OrganisationDayType,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dayTypesInFrame_RelStructure"

    day_type: Iterable[FareDayType | OrganisationDayType | DayType] = (
        field(
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
                        "type": DayType,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
