from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.add_svc import AddSvc
from travelport.models.air_exchange_bundle import AirExchangeBundle
from travelport.models.air_exchange_bundle_total import AirExchangeBundleTotal
from travelport.models.air_exchange_modifiers import AirExchangeModifiers
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.air_reservation_locator_code import (
    AirReservationLocatorCode,
)
from travelport.models.base_req_1 import BaseReq1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1
from travelport.models.host_token_1 import HostToken1
from travelport.models.optional_services import OptionalServices
from travelport.models.specific_seat_assignment import SpecificSeatAssignment
from travelport.models.ssrinfo_1 import Ssrinfo1
from travelport.models.ticket_number_1 import TicketNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirExchangeReq(BaseReq1):
    """
    Request to exchange an itinerary.

    Parameters
    ----------
    air_reservation_locator_code
        Identifies the PNR locator code. Providers ACH/1G/1V/1P
    ticket_number
    specific_seat_assignment
        Identifies the standard seat. Providers ACH/1G/1V/1P
    air_pricing_solution
        Providers ACH/1G/1V/1P.
    air_exchange_modifiers
        Provider: ACH.
    air_exchange_bundle_total
        Provider: 1G/1V/1P/1S/1A.
    air_exchange_bundle
        Bundle exchange, pricing, and penalty information. Providers
        ACH/1G/1V/1P.
    host_token
        Encrypted data from the host. Required to send the HostToken from
        the AirExchangeQuoteRsp in the AirExchangeReq. Providers
        ACH/1G/1V/1P
    optional_services
        Provider: ACH.
    form_of_payment
        Form of Payment for any additional collection charges for the
        Exchange. For ACH, most carriers will only allow refund amounts to
        the original form of payment. Providers ACH/1G/1V/1P
    form_of_payment_ref
        Provider: ACH-Universal Record reference to Form of Payment for any
        Additional Collection charges or Refund due for the itinerary
        exchange
    ssrinfo
        Providers ACH, 1G, 1V, 1P.
    add_svc
        1P - Add SVC segments to collect additional fee
    return_reservation
        Provider: ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: AirReservationLocatorCode = field(
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
        }
    )
    ticket_number: list[TicketNumber1] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    specific_seat_assignment: list[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    air_exchange_modifiers: None | AirExchangeModifiers = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
        },
    )
    air_exchange_bundle_total: None | AirExchangeBundleTotal = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
        },
    )
    air_exchange_bundle: list[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        },
    )
    form_of_payment: None | FormOfPayment1 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    form_of_payment_ref: None | FormOfPaymentRef1 = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    ssrinfo: list[Ssrinfo1] = field(
        default_factory=list,
        metadata={
            "name": "SSRInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    add_svc: None | AddSvc = field(
        default=None,
        metadata={
            "name": "AddSvc",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    return_reservation: bool = field(
        default=False,
        metadata={
            "name": "ReturnReservation",
            "type": "Attribute",
        },
    )
