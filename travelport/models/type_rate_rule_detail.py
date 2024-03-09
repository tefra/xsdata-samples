from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class TypeRateRuleDetail(Enum):
    """'None' returns hotel property descriptive information-supported for
    1p,1g/1v.

    'Complete' returns the complete hotel and room rate information-supported for 1p,1g/1v, 'RatePlansOnly' returns hotel rate information only - supported for 1p.
    """

    NONE = "None"
    COMPLETE = "Complete"
    RATE_PLANS_ONLY = "RatePlansOnly"
