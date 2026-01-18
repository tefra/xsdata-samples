from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_product_1 import TypeProduct1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class TypeSavedTripProductInfo:
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
    """

    class Meta:
        name = "typeSavedTripProductInfo"

    product_type: TypeProduct1 = field(
        metadata={
            "name": "ProductType",
            "type": "Attribute",
            "required": True,
        }
    )
    vendor_code: str = field(
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        }
    )
