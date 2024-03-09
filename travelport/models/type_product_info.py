from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_product_1 import TypeProduct1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class TypeProductInfo:
    """
    Information on the product type and its provider.

    Parameters
    ----------
    product_type
        The type of product returned
    vendor_code
        The code of the vendor. For Air, Car and Hotel this will be an IATA
        vendor code.
    provider_code
    provider_locator_code
    """

    class Meta:
        name = "typeProductInfo"

    product_type: None | TypeProduct1 = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Attribute",
            "required": True,
        },
    )
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
        },
    )
