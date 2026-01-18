from __future__ import annotations

from dataclasses import dataclass

from travelport.models.air_search_req import AirSearchReq

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ScheduleSearchReq(AirSearchReq):
    """
    Schedule Search request.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
