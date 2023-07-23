from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.base_core_req_1 import BaseCoreReq1
from travelport.models.original_itinerary_details import OriginalItineraryDetails
from travelport.models.override_pcc_1 import OverridePcc1
from travelport.models.repricing_modifiers import RepricingModifiers

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaseAirExchangeMultiQuoteReq(BaseCoreReq1):
    """
    Parameters
    ----------
    ticket_number
    provider_reservation_info
        Provider: 1P - Represents a valid Provider Reservation/PNR whose
        itinerary is to be exchanged
    air_pricing_solution
    repricing_modifiers
    original_itinerary_details
    override_pcc
    """
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
    provider_reservation_info: None | BaseAirExchangeMultiQuoteReq.ProviderReservationInfo = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 2,
        }
    )
    repricing_modifiers: None | RepricingModifiers = field(
        default=None,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    original_itinerary_details: None | OriginalItineraryDetails = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    override_pcc: None | OverridePcc1 = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
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
            }
        )
        provider_locator_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            }
        )
        supplier_code: None | str = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 5,
            }
        )
