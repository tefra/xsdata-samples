from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.associated_remark_4 import AssociatedRemark4
from travelport.models.base_reservation_1 import BaseReservation1
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.passive_remark import PassiveRemark
from travelport.models.passive_segment import PassiveSegment
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.third_party_information_1 import ThirdPartyInformation1

__NAMESPACE__ = "http://www.travelport.com/schema/passive_v52_0"


@dataclass
class PassiveReservation(BaseReservation1):
    """
    The parent container for all passive booking data.

    Parameters
    ----------
    supplier_locator
    third_party_information
    booking_traveler_ref
    passive_segment
    passive_remark
    associated_remark
    provider_reservation_info_ref
        Provider Reservation reference key.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    third_party_information: list[ThirdPartyInformation1] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    passive_segment: list[PassiveSegment] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    passive_remark: list[PassiveRemark] = field(
        default_factory=list,
        metadata={
            "name": "PassiveRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    associated_remark: list[AssociatedRemark4] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "required": True,
        }
    )
