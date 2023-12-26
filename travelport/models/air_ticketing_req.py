from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_base_req import AirBaseReq
from travelport.models.air_segment_ticketing_modifiers import (
    AirSegmentTicketingModifiers,
)
from travelport.models.air_ticketing_modifiers import AirTicketingModifiers
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.commission_1 import Commission1
from travelport.models.detailed_billing_information import (
    DetailedBillingInformation,
)
from travelport.models.fax_details_information import FaxDetailsInformation
from travelport.models.type_ticketing_modifiers_ref import (
    TypeTicketingModifiersRef,
)
from travelport.models.waiver_code import WaiverCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirTicketingReq(AirBaseReq):
    """
    Request to ticket a previously stored reservation.

    Parameters
    ----------
    air_reservation_locator_code
        Provider: 1G,1V,1P.
    air_pricing_info_ref
        Provider: 1G,1V,1P-Indicates air pricing infos to be ticketed.
    ticketing_modifiers_ref
        Provider: 1P-Reference to a shared list of Ticketing Modifiers. This
        is supported for Worldspan providers only. When AirPricingInfoRef is
        used along with TicketingModifiersRef means that particular
        TicketingModifiers will to be applied while ticketing the Stored
        fare corresponding to the AirPricingInfo. Absence of
        AirPricingInfoRef means that particular TicketingModifiers will be
        applied to all Stored fares which are requested to be ticketed.
    waiver_code
    commission
    detailed_billing_information
        Provider: 1G,1V.
    fax_details_information
        Provider: 1V.
    air_ticketing_modifiers
        Provider: 1G,1V,1P.
    air_segment_ticketing_modifiers
        Provider: 1P.
    return_info_on_fail
    bulk_ticket
        Provider: 1G,1V,1P.
    validate_spanish_residency
        Provider: 1G - If set as true, Spanish Residency will be validated
        for Provisioned Customers.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    air_pricing_info_ref: list[AirTicketingReq.AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    ticketing_modifiers_ref: list[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    waiver_code: None | WaiverCode = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        },
    )
    commission: list[Commission1] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 18,
        },
    )
    detailed_billing_information: list[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fax_details_information: None | FaxDetailsInformation = field(
        default=None,
        metadata={
            "name": "FaxDetailsInformation",
            "type": "Element",
        },
    )
    air_ticketing_modifiers: list[AirTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_segment_ticketing_modifiers: list[
        AirSegmentTicketingModifiers
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    return_info_on_fail: bool = field(
        default=True,
        metadata={
            "name": "ReturnInfoOnFail",
            "type": "Attribute",
        },
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        },
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
        },
    )

    @dataclass
    class AirPricingInfoRef:
        booking_traveler_ref: list[BookingTravelerRef1] = field(
            default_factory=list,
            metadata={
                "name": "BookingTravelerRef",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "max_occurs": 9,
            },
        )
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            },
        )
