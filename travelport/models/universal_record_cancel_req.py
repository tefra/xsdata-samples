from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.file_finishing_info_1 import FileFinishingInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordCancelReq(BaseReq1):
    """
    Request to Cancel an Universal Record.

    Parameters
    ----------
    file_finishing_info
    universal_record_locator_code
        Represents a valid Universal Record locator code
    version
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    file_finishing_info: None | FileFinishingInfo1 = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
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
