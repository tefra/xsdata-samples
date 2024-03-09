from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingBaseRsp(BaseRsp1):
    """
    Context for Responses.

    Parameters
    ----------
    universal_record
    session_key
        Session Token that was used to do the transaction echoed back.
    """

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        },
    )
    session_key: None | str = field(
        default=None,
        metadata={
            "name": "SessionKey",
            "type": "Attribute",
            "required": True,
        },
    )
