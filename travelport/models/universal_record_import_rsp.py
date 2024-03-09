from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordImportRsp(BaseRsp1):
    """
    Return the new Universal Record that was created from an external reservation.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "required": True,
        },
    )
