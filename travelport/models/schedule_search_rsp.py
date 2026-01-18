from __future__ import annotations

from dataclasses import dataclass

from travelport.models.air_search_rsp import AirSearchRsp

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ScheduleSearchRsp(AirSearchRsp):
    """
    Schedule Search response.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
