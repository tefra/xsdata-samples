from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_search_req_1 import BaseSearchReq1
from travelport.models.flight_time_table_criteria import (
    FlightTimeTableCriteria,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightTimeTableReq(BaseSearchReq1):
    """
    Request for Flight Time Table.

    Parameters
    ----------
    flight_time_table_criteria
        Provider: 1G,1V.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_time_table_criteria: None | FlightTimeTableCriteria = field(
        default=None,
        metadata={
            "name": "FlightTimeTableCriteria",
            "type": "Element",
            "required": True,
        },
    )
