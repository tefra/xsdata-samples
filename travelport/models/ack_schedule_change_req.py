from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class AckScheduleChangeReq(BaseReq1):
    """
    Request to acknowledge you have received the schedule change
    notification.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_locator_code: str = field(
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        },
    )
    reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
        },
    )
    version: int = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
