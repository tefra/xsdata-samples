from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRulesFilterCategory:
    """Fare Rules Filter if requested will return rules for requested category in
    the response.

    Applicable for providers 1G,1V,1P.

    Parameters
    ----------
    category_code
        Fare Rules Filter category can be requested. Currently only '˜MIN,
        MAX, ADV, CHG, OTH' is supported. Applicable for Providers 1G,1V,1P.
    fare_info_ref
        This tells if Low Fare Finder was used.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    category_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 35,
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
