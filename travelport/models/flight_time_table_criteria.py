from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.general_time_table import GeneralTimeTable
from travelport.models.specific_time_table import SpecificTimeTable

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FlightTimeTableCriteria:
    """
    Flight Time Table Search Criteria.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    general_time_table: None | GeneralTimeTable = field(
        default=None,
        metadata={
            "name": "GeneralTimeTable",
            "type": "Element",
        },
    )
    specific_time_table: None | SpecificTimeTable = field(
        default=None,
        metadata={
            "name": "SpecificTimeTable",
            "type": "Element",
        },
    )
