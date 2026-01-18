from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.effective_date import EffectiveDate
from travelport.models.expiration_date import ExpirationDate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class UpsellSearchCriteria:
    """
    Search Element for Effective and Expiration dates.
    """

    effective_date: EffectiveDate = field(
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
            "required": True,
        }
    )
    expiration_date: ExpirationDate = field(
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
            "required": True,
        }
    )
