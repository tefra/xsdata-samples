from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class PromoCode:
    """
    A container to specify Promotional code with Provider code and Supplier
    code.

    Parameters
    ----------
    code
        To be used to specify Promotional Code.
    provider_code
        To be used to specify Provider Code.
    supplier_code
        To be used to specify Supplier Code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: str = field(
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
