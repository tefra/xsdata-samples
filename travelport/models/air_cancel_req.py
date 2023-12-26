from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment import AirSegment
from travelport.models.air_segment_ref import AirSegmentRef
from travelport.models.base_req_1 import BaseReq1
from travelport.models.continuity_check_override_1 import (
    ContinuityCheckOverride1,
)
from travelport.models.file_finishing_info_1 import FileFinishingInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class AirCancelReq(BaseReq1):
    """Air Cancel request is used to cancel all or part of an AirReservation.

    Given only a locator code, everything within the AirReservation
    would be canceled. If particular segments are specified, then only
    those segments will be canceled.

    Parameters
    ----------
    continuity_check_override
        Provider: 1G,1V,1P,ACH.
    air_reservation_locator_code
        Provider: 1G,1V,1P,ACH.
    air_segment
        Provider: 1G,1V,1P,ACH.
    air_segment_ref
        Provider: 1G,1V,1P,ACH.
    file_finishing_info
        Provider: 1G,1V,1P,ACH.
    version
        Provider: 1G,1V,1P,ACH.
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
    air_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_segment_ref: list[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        },
    )
