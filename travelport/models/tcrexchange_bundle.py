from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_info_1 import AirExchangeInfo1
from travelport.models.air_pricing_info_ref import AirPricingInfoRef
from travelport.models.fee_info import FeeInfo
from travelport.models.penalty_1 import Penalty1
from travelport.models.tax_info import TaxInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TcrexchangeBundle:
    """
    Bundle exchange, pricing, and penalty information for one ticketless
    carrier reservation Used in AirExchangeReq request and
    AirExchangeQuoteRsp response.

    Parameters
    ----------
    air_exchange_info
    air_pricing_info_ref
    fee_info
    tax_info
        Itinerary level taxes
    penalty
        Only used within an AirExchangeQuoteRsp
    tcrnumber
        The identifying number for a Ticketless Air Reservation.
    """

    class Meta:
        name = "TCRExchangeBundle"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_exchange_info: None | AirExchangeInfo1 = field(
        default=None,
        metadata={
            "name": "AirExchangeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    air_pricing_info_ref: list[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    penalty: list[Penalty1] = field(
        default_factory=list,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    tcrnumber: None | str = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Attribute",
            "required": True,
        },
    )
