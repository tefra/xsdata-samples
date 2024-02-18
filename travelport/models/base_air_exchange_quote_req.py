from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_exchange_modifiers import AirExchangeModifiers
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.base_core_req_1 import BaseCoreReq1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.host_token_1 import HostToken1
from travelport.models.optional_services import OptionalServices
from travelport.models.original_itinerary_details import (
    OriginalItineraryDetails,
)
from travelport.models.pcc import Pcc
from travelport.models.repricing_modifiers import RepricingModifiers
from travelport.models.ticket_number_1 import TicketNumber1
from travelport.models.type_fare_rule_type import TypeFareRuleType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaseAirExchangeQuoteReq(BaseCoreReq1):
    """
    Parameters
    ----------
    ticket_number
    provider_reservation_info
        Provider: 1G/1V/1P/ACH - Represents a valid Provider Reservation/PNR
        whose itinerary is to be exchanged
    air_pricing_solution
    air_exchange_modifiers
        Provider: ACH.
    host_token
        Provider: ACH.
    optional_services
        Provider: ACH.
    form_of_payment
        Provider: ACH-This would allow a user to see the fees if they are
        changing from one Form Of Payment to other .
    repricing_modifiers
    original_itinerary_details
    pcc
    fare_rule_type
        Provider: ACH.
    """

    ticket_number: list[TicketNumber1] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    provider_reservation_info: None | BaseAirExchangeQuoteReq.ProviderReservationInfo = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 2,
        },
    )
    air_exchange_modifiers: None | AirExchangeModifiers = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    repricing_modifiers: None | RepricingModifiers = field(
        default=None,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    original_itinerary_details: None | OriginalItineraryDetails = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    pcc: None | Pcc = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        },
    )

    @dataclass
    class ProviderReservationInfo:
        """
        Parameters
        ----------
        provider_code
        provider_locator_code
        supplier_code
            Represents Carrier Code for ACH PNR Retrieve.
        """

        provider_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderCode",
                "type": "Attribute",
                "required": True,
                "min_length": 2,
                "max_length": 5,
            },
        )
        provider_locator_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            },
        )
        supplier_code: None | str = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 5,
            },
        )
