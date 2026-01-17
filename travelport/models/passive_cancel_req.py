from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.file_finishing_info_1 import FileFinishingInfo1
from travelport.models.passive_segment_ref import PassiveSegmentRef

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class PassiveCancelReq(BaseReq1):
    """
    Request for cancellation of Passive reservation/segment.

    Given the ProviderReservationInfo and PassiveReservationLocatorCode ,
    it will cancel the Passive Reservation An optional attribute of 'Key'
    will enable cancellation of a particular PassiveSegment in the Passive
    Reservation.

    Parameters
    ----------
    passive_segment_ref
        PassiveSegmentRef element refers the Key of the PassiveSegment to be
        canceled.
    file_finishing_info
    passive_reservation_locator_code
        Locator Code of the passive reservation to be canceled.
    provider_code
    provider_locator_code
    version
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    passive_segment_ref: list[PassiveSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
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
    passive_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "PassiveReservationLocatorCode",
            "type": "Attribute",
            "required": True,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
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
