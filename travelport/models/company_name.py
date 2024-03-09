from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CompanyName:
    """
    Supplier info that is specific to the Unique Id.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
