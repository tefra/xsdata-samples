from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_search_rsp_1 import BaseSearchRsp1
from travelport.models.flight_time_detail import FlightTimeDetail

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FlightTimeTableRsp(BaseSearchRsp1):
    """
    Response for Flight Time Table.

    Parameters
    ----------
    flight_time_table_list
        Provider: 1G,1V.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_time_table_list: None | FlightTimeTableRsp.FlightTimeTableList = (
        field(
            default=None,
            metadata={
                "name": "FlightTimeTableList",
                "type": "Element",
            },
        )
    )

    @dataclass(kw_only=True)
    class FlightTimeTableList:
        flight_time_detail: list[FlightTimeDetail] = field(
            default_factory=list,
            metadata={
                "name": "FlightTimeDetail",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
