from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.associated_remark_4 import AssociatedRemark4
from travelport.models.passive_remark import PassiveRemark
from travelport.models.passive_segment import PassiveSegment
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.travel_compliance_data_1 import TravelComplianceData1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class PassiveAdd:
    """
    Parameters
    ----------
    passive_segment
        This represents a Passive Segment  of type Car,Hotel,
        Tour,Surface,Air etc.
    passive_remark
        This contains Remark corresponding to any PassiveSegment
    associated_remark
        This contains Associated Remark corresponding to any PassiveSegment.
    supplier_locator
        SupplierLocator to be added to the host for Air Passive.
    third_party_information
    travel_compliance_data
    reservation_locator_code
        This represents a Passive Reservation Locator Code
    booking_traveler_ref
        BookingTravelerRef will be used to specify BookingTraveler in UR.
        Currently this will be used to add TravelComplianceData. Later this
        can used for other elements which are associated with
        BookngTraveler.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    passive_segment: list[PassiveSegment] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
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
    travel_compliance_data: list[TravelComplianceData1] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
