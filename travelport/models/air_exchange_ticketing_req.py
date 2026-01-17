from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_reservation_locator_code import (
    AirReservationLocatorCode,
)
from travelport.models.air_ticketing_modifiers import AirTicketingModifiers
from travelport.models.base_req_1 import BaseReq1
from travelport.models.detailed_billing_information import (
    DetailedBillingInformation,
)
from travelport.models.ticket_number_1 import TicketNumber1
from travelport.models.type_ticketing_modifiers_ref import (
    TypeTicketingModifiersRef,
)
from travelport.models.waiver_code import WaiverCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeTicketingReq(BaseReq1):
    """
    Request to ticket an exchanged itinerary.

    Providers 1G, 1V, 1P.

    Parameters
    ----------
    air_reservation_locator_code
        Identifies the PNR to ticket. Providers 1G, 1V, 1P.
    ticket_number
        Ticket number to reissue. Providers 1G, 1V, 1P.
    ticketing_modifiers_ref
        Provider: 1P-Reference to a shared list of Ticketing Modifiers. This
        is supported for Worldspan provider only. When AirPricingInfoRef is
        used along with TicketingModifiersRef means that particular
        TicketingModifiers will to be applied while ticketing the Stored
        fare corresponding to the AirPricingInfo. Absence of
        AirPricingInfoRef means that particular TicketingModifiers will be
        applied to all Stored fares which are requested to be ticketed.
    waiver_code
    detailed_billing_information
        Providers 1G, 1V, 1P.
    air_ticketing_modifiers
        Provider: 1G,1V,1P.
    bulk_ticket
        Providers 1G, 1V, 1P.
    change_fee_on_ticket
        Applies the change fee/penalty to the original form of payment.
        Providers: 1V
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: None | AirReservationLocatorCode = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
        },
    )
    ticket_number: None | TicketNumber1 = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
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
    detailed_billing_information: list[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
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
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        },
    )
    change_fee_on_ticket: bool = field(
        default=True,
        metadata={
            "name": "ChangeFeeOnTicket",
            "type": "Attribute",
        },
    )
