from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AirUpsellDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    qualify_ref: None | str = field(
        default=None,
        metadata={
            "name": "QualifyRef",
            "type": "Attribute",
        },
    )
    offer_ref: None | str = field(
        default=None,
        metadata={
            "name": "OfferRef",
            "type": "Attribute",
        },
    )
