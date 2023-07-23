from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_base_rsp import BookingBaseRsp
from travelport.models.etr import Etr
from travelport.models.type_failure_info import TypeFailureInfo

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingRetrieveDocumentRsp(BookingBaseRsp):
    """
    Parameters
    ----------
    etr
        Provider: 1G,1V,1P.
    document_failure_info
        Provider: 1G,1V,1P -Will be optionally returned if there are
        duplicate ticket numbers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    etr: list[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    document_failure_info: list[TypeFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "DocumentFailureInfo",
            "type": "Element",
            "max_occurs": 99,
        }
    )
