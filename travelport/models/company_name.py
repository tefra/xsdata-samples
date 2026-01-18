from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class CompanyName:
    """
    Supplier info that is specific to the Unique Id.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    supplier_code: str = field(
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
