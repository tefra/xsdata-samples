from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.add_svc import AddSvc
from travelport.models.air_exchange_bundle import AirExchangeBundle
from travelport.models.air_exchange_bundle_total import AirExchangeBundleTotal
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.host_token_1 import HostToken1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingAirExchangeReq(BookingBaseReq):
    """
    Performs exchange on existing reservations.

    Parameters
    ----------
    air_reservation_locator_code
        Identifies the PNR locator code. Providers 1G/1V/1P
    ticket_number
    air_pricing_solution
        Providers ACH/1G/1V/1P.
    air_exchange_bundle_total
        Provider: 1G/1V/1P/1S/1A.
    air_exchange_bundle
        Bundle exchange, pricing, and penalty information. Providers
        ACH/1G/1V/1P.
    host_token
        Encrypted data from the host. Required to send the HostToken from
        the AirExchangeQuoteRsp in the AirExchangeReq. Providers
        ACH/1G/1V/1P
    add_svc
        1P - Add SVC segments to collect additional fee
    override_warnings
        Set to true will allow multiple end transact attempts. Set to false
        only one end transact is done and warnings are returned for follow
        up action. Supported Providers: 1G/1V
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )
    air_exchange_bundle_total: None | AirExchangeBundleTotal = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_exchange_bundle: list[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    add_svc: None | AddSvc = field(
        default=None,
        metadata={
            "name": "AddSvc",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    override_warnings: None | bool = field(
        default=None,
        metadata={
            "name": "OverrideWarnings",
            "type": "Attribute",
        }
    )
