from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class UpsellBrand:
    """
    Upsell brand reference.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
