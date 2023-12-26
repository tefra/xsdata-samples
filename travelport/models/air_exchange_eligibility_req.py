from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeEligibilityReq(BaseReq1):
    """
    Request to determine if the fares in an itinerary are exchangeable.

    Parameters
    ----------
    provider_reservation_info
        Provider:1P - Represents a valid Provider Reservation/PNR whose
        itinerary is to be exchanged
    type_value
        Type choices are "Detail" or "Summary"  Default will be Summary
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    provider_reservation_info: None | AirExchangeEligibilityReq.ProviderReservationInfo = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "required": True,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
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
