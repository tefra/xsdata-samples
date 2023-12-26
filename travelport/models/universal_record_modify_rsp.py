from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_solution_changed_info import AirSolutionChangedInfo
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_modify_failure_info import (
    UniversalModifyFailureInfo,
)
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordModifyRsp(BaseRsp1):
    """
    Return a Universal Record.

    Parameters
    ----------
    universal_record
    air_solution_changed_info
    universal_modify_failure_info
    queue_session_token
        Queue Session Token to hold session token for multiple queue
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        },
    )
    air_solution_changed_info: list[AirSolutionChangedInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    universal_modify_failure_info: None | UniversalModifyFailureInfo = field(
        default=None,
        metadata={
            "name": "UniversalModifyFailureInfo",
            "type": "Element",
        },
    )
    queue_session_token: None | str = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        },
    )
