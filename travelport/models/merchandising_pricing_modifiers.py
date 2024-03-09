from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_code_1 import AccountCode1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class MerchandisingPricingModifiers:
    """
    Parameters
    ----------
    account_code
        The account code is used to get corporate discounted pricing on paid
        seats. Provider:ACH
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    account_code: list[AccountCode1] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 10,
        },
    )
