from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.continuity_check_override_1 import (
    ContinuityCheckOverride1,
)
from travelport.models.file_finishing_info_1 import FileFinishingInfo1
from travelport.models.queue_next_modifiers import QueueNextModifiers
from travelport.models.record_identifier import RecordIdentifier
from travelport.models.universal_modify_cmd import UniversalModifyCmd

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordModifyReq(BaseReq1):
    """
    Update the universal record.

    Parameters
    ----------
    continuity_check_override
    record_identifier
    universal_modify_cmd
    file_finishing_info
    queue_next_modifiers
    return_record
        Either the updated UniversalRecord or Universal Record for next on
        queue should be returned in the response
    version
    override_mct
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    continuity_check_override: None | ContinuityCheckOverride1 = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    record_identifier: None | RecordIdentifier = field(
        default=None,
        metadata={
            "name": "RecordIdentifier",
            "type": "Element",
            "required": True,
        },
    )
    universal_modify_cmd: list[UniversalModifyCmd] = field(
        default_factory=list,
        metadata={
            "name": "UniversalModifyCmd",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    file_finishing_info: None | FileFinishingInfo1 = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    queue_next_modifiers: None | QueueNextModifiers = field(
        default=None,
        metadata={
            "name": "QueueNextModifiers",
            "type": "Element",
        },
    )
    return_record: bool = field(
        default=False,
        metadata={
            "name": "ReturnRecord",
            "type": "Attribute",
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        },
    )
    override_mct: bool = field(
        default=False,
        metadata={
            "name": "OverrideMCT",
            "type": "Attribute",
        },
    )
