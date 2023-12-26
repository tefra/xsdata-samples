from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class TypeProviderReservationDetail1:
    """Details of a provider reservation locator consisting of provider locator
    code and provider code.

    To be used as a request element type while accessing a specific PNR

    Parameters
    ----------
    provider_code
    provider_locator_code
    supplier_code
        Represents Carrier Code for ACH PNR Retrieve.
    """

    class Meta:
        name = "typeProviderReservationDetail"

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
