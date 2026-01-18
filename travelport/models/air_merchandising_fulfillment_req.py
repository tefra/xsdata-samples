from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agency_payment_1 import AgencyPayment1
from travelport.models.agency_sell_info_1 import AgencySellInfo1
from travelport.models.air_solution import AirSolution
from travelport.models.base_req_1 import BaseReq1
from travelport.models.credit_card_1 import CreditCard1
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.host_reservation import HostReservation
from travelport.models.host_token_1 import HostToken1
from travelport.models.merchandising_pricing_modifiers import (
    MerchandisingPricingModifiers,
)
from travelport.models.optional_services import OptionalServices
from travelport.models.specific_seat_assignment import SpecificSeatAssignment

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class AirMerchandisingFulfillmentReq(BaseReq1):
    """
    This will fulfill the merchandised items as specified in the request.

    The host PNR will be updated with the services and any required charges
    will be added.

    Parameters
    ----------
    host_token
        Provider: ACH.
    host_reservation
        Provider: 1G,1V,1P,ACH.
    agency_sell_info
        Provider: 1G,1V,1P,ACH.
    air_solution
        Provider: 1G,1V,1P,ACH.
    credit_card
        Provider: 1G,1V,1P,ACH.
    agency_payment
        Provider: ACH
    optional_services
    specific_seat_assignment
        Provider: 1G,1V,1P,ACH.
    general_remark
        Provider: 1G,1V,1P,ACH.
    confirmation_email
        Provider: 1G,1V,1P,ACH.
    merchandising_pricing_modifiers
        Used to provide additional pricing modifiers. Provider:ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    host_reservation: list[HostReservation] = field(
        default_factory=list,
        metadata={
            "name": "HostReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    agency_sell_info: None | AgencySellInfo1 = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    air_solution: AirSolution = field(
        metadata={
            "name": "AirSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        }
    )
    credit_card: None | CreditCard1 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    agency_payment: None | AgencyPayment1 = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    specific_seat_assignment: list[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark1] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    confirmation_email: None | str = field(
        default=None,
        metadata={
            "name": "ConfirmationEmail",
            "type": "Element",
        },
    )
    merchandising_pricing_modifiers: None | MerchandisingPricingModifiers = (
        field(
            default=None,
            metadata={
                "name": "MerchandisingPricingModifiers",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
    )
