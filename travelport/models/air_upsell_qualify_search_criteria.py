from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_code_1 import AccountCode1
from travelport.models.upsell_search_criteria import UpsellSearchCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class AirUpsellQualifySearchCriteria(UpsellSearchCriteria):
    """
    Search criteria for AirUpsellQualify.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    account_code: None | AccountCode1 = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    carrier: str = field(
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
