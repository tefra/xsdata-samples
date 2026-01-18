from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_low_fare_search_req import BaseLowFareSearchReq

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class LowFareSearchReq(BaseLowFareSearchReq):
    """
    Low Fare Search request.

    Parameters
    ----------
    policy_reference
        This attribute will be used to pass in a value on the request which
        would be used to link to a ‘Policy Group’ in a policy engine
        external to UAPI.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    policy_reference: None | str = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
