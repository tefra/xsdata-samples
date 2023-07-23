from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment import AirSegment
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.cabin_class_1 import CabinClass1
from travelport.models.host_token_1 import HostToken1
from travelport.models.optional_services import OptionalServices
from travelport.models.payment_restriction_1 import PaymentRestriction1
from travelport.models.remark_1 import Remark1
from travelport.models.rows import Rows
from travelport.models.search_traveler import SearchTraveler
from travelport.models.seat_information import SeatInformation

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SeatMapRsp(BaseRsp1):
    """
    Parameters
    ----------
    host_token
        Provider: ACH,MCH.
    cabin_class
        Provider: 1G,1V,1P,ACH,MCH.
    air_segment
        Provider: ACH,MCH.
    search_traveler
        Provider: ACH,MCH.
    optional_services
        A wrapper for all the information regarding each of the Optional
        Services. Provider: 1G,1V,1P,ACH.
    remark
        Provider: 1G,1V,1P,ACH,MCH.
    rows
    payment_restriction
        Provider: MCH-Information regarding valid payment types, if
        restrictions apply(supplier specific)
    seat_information
    copyright
        Copyright text applicable for some seat content. Providers: 1G, 1V,
        1P,ACH
    group_seat_price
        Provider: 1G,1V-Seat price for the all passengers traveling together
        only when supplier provides group flat fee.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    cabin_class: None | CabinClass1 = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    search_traveler: list[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    remark: None | Remark1 = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rows: list[Rows] = field(
        default_factory=list,
        metadata={
            "name": "Rows",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    payment_restriction: list[PaymentRestriction1] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    seat_information: list[SeatInformation] = field(
        default_factory=list,
        metadata={
            "name": "SeatInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    copyright: None | str = field(
        default=None,
        metadata={
            "name": "Copyright",
            "type": "Element",
        }
    )
    group_seat_price: None | str = field(
        default=None,
        metadata={
            "name": "GroupSeatPrice",
            "type": "Attribute",
        }
    )
