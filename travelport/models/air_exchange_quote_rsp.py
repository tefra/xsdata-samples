from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_exchange_bundle import AirExchangeBundle
from travelport.models.air_exchange_bundle_total import AirExchangeBundleTotal
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.fare_rule import FareRule
from travelport.models.host_token_1 import HostToken1
from travelport.models.optional_services import OptionalServices
from travelport.models.ticket_number_1 import TicketNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeQuoteRsp(BaseRsp1):
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
    optional_services
        Provider: ACH.
    fare_rule
        Provider: ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_number: list[TicketNumber1] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    fare_rule: list[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        },
    )
