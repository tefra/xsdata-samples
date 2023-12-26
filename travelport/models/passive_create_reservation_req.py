from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.action_status_1 import ActionStatus1
from travelport.models.associated_remark_4 import AssociatedRemark4
from travelport.models.base_create_reservation_req_1 import (
    BaseCreateReservationReq1,
)
from travelport.models.passive_remark import PassiveRemark
from travelport.models.passive_segment import PassiveSegment
from travelport.models.review_booking_1 import ReviewBooking1
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.third_party_information_1 import ThirdPartyInformation1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class PassiveCreateReservationReq(BaseCreateReservationReq1):
    """
    Request to create a passive reservation.

    Parameters
    ----------
    supplier_locator
    third_party_information
    passive_segment
    passive_remark
    associated_remark
    action_status
    review_booking
        Review Booking or Queue Minders is to add the reminders in the
        Provider Reservation along with the date time and Queue details. On
        the date time defined in reminders, the message along with the PNR
        goes to the desired Queue.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    third_party_information: list[ThirdPartyInformation1] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    passive_segment: list[PassiveSegment] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    passive_remark: list[PassiveRemark] = field(
        default_factory=list,
        metadata={
            "name": "PassiveRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        },
    )
    associated_remark: list[AssociatedRemark4] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        },
    )
    action_status: None | ActionStatus1 = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    review_booking: list[ReviewBooking1] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
