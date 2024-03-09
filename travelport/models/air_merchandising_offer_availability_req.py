from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agency_sell_info_1 import AgencySellInfo1
from travelport.models.air_solution import AirSolution
from travelport.models.base_req_1 import BaseReq1
from travelport.models.host_reservation import HostReservation
from travelport.models.merchandising_pricing_modifiers import (
    MerchandisingPricingModifiers,
)
from travelport.models.offer_availability_modifiers import (
    OfferAvailabilityModifiers,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirMerchandisingOfferAvailabilityReq(BaseReq1):
    """
    Check with the supplier whether or not the reservation or air solution supports
    any merchandising offerings.

    Parameters
    ----------
    agency_sell_info
        Provider: 1G,1V,1P,ACH.
    air_solution
        Provider: 1G,1V,1P,ACH.
    host_reservation
        Provider: 1G,1V,1P,ACH.
    offer_availability_modifiers
        Provider: 1G,1V,1P,ACH.
    merchandising_pricing_modifiers
        Used to provide additional pricing modifiers. Provider:ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    agency_sell_info: None | AgencySellInfo1 = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    air_solution: None | AirSolution = field(
        default=None,
        metadata={
            "name": "AirSolution",
            "type": "Element",
        },
    )
    host_reservation: list[HostReservation] = field(
        default_factory=list,
        metadata={
            "name": "HostReservation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    offer_availability_modifiers: list[OfferAvailabilityModifiers] = field(
        default_factory=list,
        metadata={
            "name": "OfferAvailabilityModifiers",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    merchandising_pricing_modifiers: None | MerchandisingPricingModifiers = (
        field(
            default=None,
            metadata={
                "name": "MerchandisingPricingModifiers",
                "type": "Element",
            },
        )
    )
