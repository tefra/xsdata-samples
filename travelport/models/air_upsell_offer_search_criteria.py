from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_code_1 import AccountCode1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AirUpsellOfferSearchCriteria:
    """
    Search criteria for AirUpsellOffers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    account_code: None | AccountCode1 = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )
