from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.brand import Brand
from travelport.models.optional_services import OptionalServices
from travelport.models.type_applicable_segment import TypeApplicableSegment

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirMerchandisingDetailsRsp(BaseRsp1):
    """
    Response for retrieved brand details and optional services included in them.

    Parameters
    ----------
    optional_services
    brand
    unassociated_booking_code_list
        Lists classes of service by segment sent in the request which are
        not associated to a brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    brand: list[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    unassociated_booking_code_list: None | AirMerchandisingDetailsRsp.UnassociatedBookingCodeList = field(
        default=None,
        metadata={
            "name": "UnassociatedBookingCodeList",
            "type": "Element",
        }
    )

    @dataclass
    class UnassociatedBookingCodeList:
        applicable_segment: list[TypeApplicableSegment] = field(
            default_factory=list,
            metadata={
                "name": "ApplicableSegment",
                "type": "Element",
                "max_occurs": 99,
            }
        )
