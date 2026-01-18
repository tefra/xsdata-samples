from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_bundle import AirExchangeBundle
from travelport.models.air_exchange_bundle_total import AirExchangeBundleTotal
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.booking_base_rsp import BookingBaseRsp
from travelport.models.host_token_1 import HostToken1
from travelport.models.ticket_number_1 import TicketNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class BookingAirExchangeQuoteRsp(BookingBaseRsp):
    """
    Parameters
    ----------
    ticket_number
    air_pricing_solution
        Provider: 1G/1V/1P/1S/1A.
    air_exchange_bundle_total
    air_exchange_bundle
        Bundle exchange, pricing, and penalty information. Providers
        ACH/1G/1V/1P
    host_token
        Encrypted data from the host. Required to send the HostToken from
        the AirExchangeQuoteRsp in the AirExchangeReq. Providers
        ACH/1G/1V/1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    ticket_number: list[TicketNumber1] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
    air_exchange_bundle_total: None | AirExchangeBundleTotal = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    air_exchange_bundle: list[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        },
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
